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
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('design-challenge', views.design_challenge, name='design_challenge'),
    path('cinema-4d', views.cinema_4d, name='cinema-4d'),
    path('hackathon', views.hackathon, name='hackathon'),
    path('roku-themes', views.roku_themes, name='roku-themes'),
    path('guest-mode', views.guest_mode, name='guest-mode'),
    path('roku-zones', views.roku_zones, name='roku-zones'),
    path('voice-search', views.voice_search, name='voice-search'),
    path('pet-to-you', views.pet_to_you, name='pet-to-you'),
    path('personalized_activation', views.personalized_activation, name='personalized_activation'),
    path('game_console_configuration', views.game_console_configuration, name='game_console_configuration'),
    path('design-challenge-template', views.design_challenge_template, name='design_challenge_template'),
    
    #old pages
    path('catrait', views.catrait, name='catrait'),
    path('LeECO_Design_Challenge', views.LeECO_Design_Challenge, name='LeECO_Design_Challenge'), #hulu
    path('fine_art', views.fine_art, name='fine_art'),
    path('landscape_temp112560123254', views.landscape_temp112560123254, name='landscape_temp112560123254'),
    path('package', views.package, name='package'),
    path('skype', views.skype, name='skype'),
    path('infographics', views.infographics, name='infographics'),
    path('leantaas_mock_up', views.leantaas_mock_up, name='leantaas_mock_up'),
    path('personal_branding', views.personal_branding, name='personal_branding'),
    path('wabash', views.wabash, name='wabash'),
    path('chummy', views.chummy, name='chummy'),
    path('landscape', views.landscape, name='landscape'),
    path('leantaas', views.leantaas, name='leantaas'),
    
#    Removed pages:    
#    path('product_design', views.product_design, name='product_design'),
    
#    Login pages:
#    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
#    path('logout', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
#    Admin pages:
#    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
