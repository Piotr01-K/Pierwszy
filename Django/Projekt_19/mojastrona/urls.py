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
from django.urls import path
from ogloszenia.views import home_view, product_list_view
#   from mojastrona.views import info_view, rules_view, user_profile_view
#   from ogloszenia import views    #  dodane w ramach task 1 (lesson20)
#   from . import views   #  dodane w ramach task 2 (lesson 20)
from mojastrona import views as project_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("", home_view, name="home"),
#     path('info/', views.info_view, name='info'),   # dodane w ramach task 1 (lesson 20)
#     path('rules/', views.rules_view, name='rules'),   # dodane w ramach task 1 (lesson 20)
#     path('user/<str:username>/', views.user_profile_view, name='user-profile'),   # dodane w ramach task 2 (lesson 20)
#     path('produkty/', views.product_list_view, name='product-list'),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('info/', project_views.info_view, name='info'),
    path('rules/', project_views.rules_view, name='rules'),
    path('user/<str:username>/', project_views.user_profile_view, name='user-profile'),
    path('produkty/', product_list_view, name='product-list'),
]
