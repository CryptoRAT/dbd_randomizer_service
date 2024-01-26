from django.urls import re_path
from . import views as perk_views

urlpatterns = [
    re_path('survivor/random', perk_views.RandomSurvivorPerkView.as_view({'post': 'random'}),  name='random-survivor-perks'),
    re_path('killer/random', perk_views.RandomKillerPerkView.as_view({'post': 'random'}), name='random-killer-perks'),
    re_path('survivor', perk_views.PerkView.as_view({'get': 'list'}), name='survivor-perks'),
    re_path('killer', perk_views.KillerPerkView.as_view({'get': 'list'}), name='killer-perks'),
]




