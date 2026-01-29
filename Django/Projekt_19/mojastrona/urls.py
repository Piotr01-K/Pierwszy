"""
URL configuration for mojastrona project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
#   from tasks.views import ProductViewSet   #  zahashowane przy task 3 lesson 25
from products.views import ProductViewSet   #  dodane w ramach task 3 lesson 25
from tasks.views import set_name, hello   #  dodane w ramach task 5 lesson 25
from notes.views import NoteViewSet     #  dodane w ramach task 6 lesson 25
from tasks.views import calculate     #  dodane w ramach task 7 lesson 25
from products.views import AuthorViewSet, BookViewSet    #  dodane w ramach task 9 lesson 25

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'notes', NoteViewSet)    #  dodane w ramach task 6 lesson 25
router.register(r'authors', AuthorViewSet)   #  dodane w ramach task 9 lesson 25
router.register(r'books', BookViewSet)    #  dodane w ramach task 9 lesson 25

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/set-name/', set_name),    #  dodane w ramach task 5 lesson 25
    path('api/hello/', hello),    #  dodane w ramach task 5 lesson 25
    path('api/calculate/', calculate),    #  dodane w ramach task 7 lesson 25
]
