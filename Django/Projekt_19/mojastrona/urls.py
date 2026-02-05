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
from django.urls import path, include   #   dodane "include" w Task 2 lesson 24
from ogloszenia.views import home_view, product_list_view
#   from mojastrona.views import info_view, rules_view, user_profile_view
#   from ogloszenia import views    #  dodane w ramach task 1 (lesson20) /  zahashowane znowu przy task 3 lesson 24
from . import views   #  dodane w ramach task 2 (lesson 20) zahashowane przy innym zadaniu i wznowione ponownie przy task 3 lesson 24
#   from mojastrona import views as project_views   #  zahashowane przy task 3 lesson 24
from ogloszenia.views import categories_list_view    # dodane w ramach Task 3 Lesson 21
#   from ogloszenia import views    # dodane w ramach Task 6 Lesson 21 / zahashowane znowu przy task 3 lesson 24
from ogloszenia.views import article_list_view   # dodane w ramach Task 8 Lesson 21
from ogloszenia.views import ArticleListView    # dodane w ramach Task 9 Lesson 22
from ogloszenia.views import statistics_view    # dodane w ramach Task 10 lesson 22
from django.conf import settings     # dodane w ramach lesson 23 (przygotowanie do aplikacji "cars")
from django.conf.urls.static import static    # dodane w ramach lesson 23 (przygotowanie do aplikacji "cars")
from django.contrib.auth import views as auth_views   # dodane w ramach Task 8 lesson 24 (auth_views zamiast views.py dla uniknięcia konfliktu)
from mojastrona import views   # dodane w ramach Task 10 lesson 24

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
    path('info/', views.info_view, name='info'),
    path('rules/', views.rules_view, name='rules'),
    path('user/<str:username>/', views.user_profile_view, name='user-profile'),
    path('produkty/', product_list_view, name='product-list'),
    #   path('about/', views.about_view, name='about'),    #  dodałem w ramach task 5 lesson 20 / zahashowane przy task 3 lesson 24
    path('categories/', categories_list_view, name='categories-list'),    #  dodałem w ramach task 3 lesson 21
    #   path('categories/<int:pk>/', views.category_detail_view, name='category-detail'),    # dodałem w ramach task 6 lesson 21 / # przy task 3 lesson 24
    path('articles/', article_list_view, name='article-list'),   # dodałem w ramach task 8 lesson 21
    #   path('blog/<int:blog_id>/entries/', views.blog_entries_view, name='blog-entries'),    # dodałem w ramach task 4 lesson 22 / # przy task 3 lesson 24
    #   path('contact/', views.contact_view, name='contact'),     # dodałem w ramach task 6 lesson 22 / # przy task 3 lesson 24
    path('articles/', ArticleListView.as_view(), name='article_list'),    # dodałem w ramach task 9 lesson 22
    path('statistics/', statistics_view, name='statistics'),   # dodane w ramach Task 10 lesson 22
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),    # dodane w ramach Task 2 lesson 24
    path('profile/', views.profile, name='profile'),    # dodane w ramach Task 3 lesson 24
    path('register/', views.register, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change_form.html'
    ), name='password_change'),     # dodane w ramach Task 8 lesson 24
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'
    ), name='password_change_done'),     # dodane w ramach Task 8 lesson 24
    #   path("admin/users/", views.users_list, name="users-list"),     # dodane w ramach Task 10 lesson 24
    path('users/', views.users_list, name='users-list'),    # dodane w ramach Task 10 lesson 24
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

