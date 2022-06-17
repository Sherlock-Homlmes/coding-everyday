"""bettermenews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from .views import zzz_admin_page, zzz_oauth, zzz_page_content
from .views import zzz_oauth

urlpatterns = [
    #path('hello/',zzz_admin_page.hello,name="hello"),

    #login
    path('discord_oauth/',zzz_oauth.discord_oauth,name="discord-oauth"),
    path('logout/',zzz_oauth.logout,name="discord-logout"),
   
    #page content
    path('', zzz_page_content.home,name="index"),
    path('<str:name>/',zzz_page_content.topic_post,name="topic-post"),
    
    #scraping web
    path('auto-scrap/<int:page_number>',zzz_admin_page.auto_scrap,name="auto-scrap"),
    path('auto-scrap/check-content/<str:name>',zzz_admin_page.scrap_check,name="scrap-check"),
    path('auto-scrap/confirm/',zzz_admin_page.scrap_confirm,name="scrap-check"),
    #path('/auto-scrap/confirm'),
]
