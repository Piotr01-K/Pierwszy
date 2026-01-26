from django.urls import path, include
from .views import ProtectedView
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')

urlpatterns = [
    path('protected/', ProtectedView.as_view()),
    path('', include(router.urls)),
    ]
