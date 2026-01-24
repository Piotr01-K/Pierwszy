
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Djoser – rejestracja użytkowników  (dodane task 4 lesson 26)
    path('auth/', include('djoser.urls')),

    # JWT – logowanie, refresh tokenu   (dodane task 4 lesson 26)
    path('auth/', include('djoser.urls.jwt')),

    path('api/', include('accounts.urls')), # dodane task 8 lesson 26
]
