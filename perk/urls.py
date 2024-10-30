from django.urls import re_path
from . import views as perk_views

urlpatterns = [
    re_path(r'^survivor/random$', perk_views.RandomSurvivorPerkView.as_view({'post': 'random'}),  name='random-survivor-perks'),
    re_path(r'^killer/random$', perk_views.RandomKillerPerkView.as_view({'post': 'random'}), name='random-killer-perks'),
    re_path(r'^survivor$', perk_views.PerkView.as_view({'get': 'list', 'post': 'create'}), name='survivor-perks'),
    re_path(r'^killer$', perk_views.KillerPerkView.as_view({'get': 'list'}), name='killer-perks'),
    re_path(r'^(?P<pk>\d+)/$', perk_views.PerkView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='perk-detail'),
]
