
from django.contrib import admin
from django.urls import path, include
from accounts.views import ProtectedView   # dodane w ramach task 9 lesson 26

urlpatterns = [
    path('admin/', admin.site.urls),

    # Djoser – rejestracja użytkowników  (dodane task 4 lesson 26)
    path('auth/', include('djoser.urls')),

    # JWT – logowanie, refresh tokenu   (dodane task 4 lesson 26)
    path('auth/', include('djoser.urls.jwt')),

    path('api/', include('accounts.urls')), # dodane task 8 lesson 26
    path("protected/", ProtectedView.as_view()),   # dodane task 9 lesson 26
    path('__debug__/', include('debug_toolbar.urls')),   # dodane task 2 lesson 27
]
