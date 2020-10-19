"""djangomodelform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_post/', views.add_post, name='add_post'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_article/', views.add_article, name='add_article'),
    path('add_reporter/', views.add_reporter, name='add_reporter'),
    path('list_authors/', views.list_authors, name='list_authors'),
    path('list_books/', views.list_books, name='list_books'),
    path('list_reporters/', views.list_reporters, name='list_reporters'),
    path('list_articles/', views.list_articles, name='list_articles'),
    path('', views.list_posts, name='list_posts'),
]
