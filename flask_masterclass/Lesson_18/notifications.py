# notifications.py
from datetime import datetime, timedelta
from sqlalchemy import and_
from models import Booking, Notification, db  # Booking musi być w models.py
from app import db

def create_reminder_notification_for_booking(booking):
    """
    Utworzy Notification dla użytkownika (booking.user_id)
    z wiadomością przypominającą o rezerwacji 1 godzinę przed.
    Nie zapisuje w sesji — zwraca obiekt Notification.
    """
    msg = f"Przypomnienie: Twoja rezerwacja sali (ID {booking.id}) zaczyna się o {booking.start_time}."
    return Notification(
        user_id=booking.user_id,
        message=msg,
        is_read=False,
        created_at=datetime.utcnow()
    )

def find_bookings_starting_in_one_hour(session):
    """
    Zwraca listę rezerwacji, które zaczynają się ~1h od teraz.
    Korzysta z SQLAlchemy session (tutaj db.session) i pola Booking.start_time.
    Zakładam, że model Booking ma pole start_time typu datetime.
    """
    now = datetime.utcnow()
    in_one_hour = now + timedelta(hours=1)
    # Szukamy bookingów, których start_time jest między teraz+59min a teraz+61min
    window_start = in_one_hour - timedelta(minutes=1)
    window_end = in_one_hour + timedelta(minutes=1)

    return session.query(Booking).filter(
        and_(
            Booking.start_time >= window_start,
            Booking.start_time <= window_end
        )
    ).all()

def create_reminders_now():
    """
    Funkcja, którą można wywołać okresowo (scheduler).
    Sprawdza bookingi, tworzy przypomnienia (jeśli jeszcze nie istnieją)
    i zapisuje je do bazy.
    """
    session = db.session
    bookings = find_bookings_starting_in_one_hour(session)
    created = 0
    for b in bookings:
        # (opcjonalnie) sprawdź czy już istnieje przypomnienie dla tego booking.id
        exists = session.query(Notification).filter(
            Notification.user_id == b.user_id,
            Notification.message.like(f"%rezerwacja sali (ID {b.id})%")
        ).first()
        if exists:
            continue
        notif = create_reminder_notification_for_booking(b)
        session.add(notif)
        created += 1
    if created:
        session.commit()
    return created
