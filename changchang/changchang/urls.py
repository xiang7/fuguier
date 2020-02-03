"""changchang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from web import views
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('design-challenge', views.design_challenge, name='design_challenge'),
    path('hackathon', views.hackathon, name='hackathon'),
    path('cinema-4d', views.cinema_4d, name='cinema-4d'),
    path('roku-themes', views.roku_themes, name='roku-themes'),
    path('guest-mode', views.guest_mode, name='guest-mode'),
    path('roku-zones', views.roku_zones, name='roku-zones'),
    path('voice-search', views.voice_search, name='voice-search'),
    path('pet-to-you', views.pet_to_you, name='pet-to-you'),
    path('design-challenge-template', views.design_challenge_template, name='design_challenge_template'),
    
#    Login pages:
#    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
#    path('logout', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
#    Admin pages:
#    path('admin/', admin.site.urls),
]
