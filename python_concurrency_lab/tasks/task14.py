import threading
import shutil
from pathlib import Path


def kopiuj_plik(plik_zrodlowy, katalog_docelowy):
    print(f"Kopiowanie pliku {plik_zrodlowy.name}...")
    shutil.copy2(plik_zrodlowy, katalog_docelowy)
    print(f"Ukończono kopiowanie pliku {plik_zrodlowy.name}")


def main():
    # Katalog, w którym znajduje się ten plik (tasks/)
    katalog_tasks = Path(__file__).parent

    # Katalog główny projektu (python_concurrency_lab/)
    katalog_glowny = katalog_tasks.parent

    # Katalog z plikami źródłowymi
    katalog_zrodlowy = katalog_glowny / "source_files"

    # Katalog docelowy
    katalog_docelowy = katalog_glowny / "target_files"

    watki = []

    # Iterujemy po WSZYSTKICH plikach w source_files
    for plik in katalog_zrodlowy.iterdir():
        if plik.is_file():
            watek = threading.Thread(
                target=kopiuj_plik,
                args=(plik, katalog_docelowy)
            )
            watki.append(watek)
            watek.start()

    # Czekamy, aż wszystkie wątki zakończą pracę
    for watek in watki:
        watek.join()

    print("Wszystkie pliki zostały skopiowane.")


if __name__ == "__main__":
    main()
