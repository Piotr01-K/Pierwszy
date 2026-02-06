
from django.contrib import admin
from django.urls import path, include
from accounts.views import ProtectedView   # dodane w ramach task 9 lesson 26
from accounts.views import SelectiveCacheView   # dodane w ramach task 7 lesson 27
from rest_framework_simplejwt.views import (    # dodane w ramach task 9 lesson 27
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings    # dodane w ramach task 14 lesson 29
from django.conf.urls.static import static   # dodane w ramach task 14 lesson 29

urlpatterns = [
    path('admin/', admin.site.urls),

    # Djoser – rejestracja użytkowników  (dodane task 4 lesson 26)
    path('auth/', include('djoser.urls')),

    # JWT – logowanie, refresh tokenu   (dodane task 4 lesson 26)
    path('auth/', include('djoser.urls.jwt')),

    path('api/', include('accounts.urls')), # dodane task 8 lesson 26
    path("protected/", ProtectedView.as_view()),   # dodane task 9 lesson 26
    path('__debug__/', include('debug_toolbar.urls')),   # dodane task 2 lesson 27
    path('selective-cache/', SelectiveCacheView.as_view()),   # dodane task 7 lesson 27
    path('', include('accounts.urls')),  # dodane task 8 lesson 27
    path('auth/jwt/create/', TokenObtainPairView.as_view(), name='jwt_create'),    # dodane w ramach task 9 lesson 27
    path('auth/jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),    # dodane w ramach task 9 lesson 27
    path('api/core/', include('core.urls')),  # dodane w ramach Task 1 Lesson 29
    path("core/", include("core.urls")),  # dodane w ramach Task 1 Lesson 29
    path('api/auth/jwt/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('core.urls')),
    ]

 # dodane w ramach task 14 lesson 29
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
