"""
URL configuration for dbd_randomizer_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import re_path, reverse, include
from rest_framework import routers
from survivor import views as survivor_views
from perk import views as perk_views

router = routers.DefaultRouter()
router.register(r'survivor/perks/random', perk_views.RandomSurvivorPerkView, 'random-survivor-perks')
router.register(r'killer/perks/random', perk_views.RandomKillerPerkView, 'random-killer-perks')
router.register(r'survivor/random', survivor_views.RandomSurvivorView, 'random-survivor')
router.register(r'survivor/perks', perk_views.PerkView, 'survivor-perks')  # Updated endpoint for CRUD operations
router.register(r'killer/perks', perk_views.KillerPerkView, 'killer-perks')
router.register(r'survivor', survivor_views.SurvivorView, 'survivor')

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('api/', include(router.urls)),
]
