from django.urls import re_path
from . import views as killer_views

urlpatterns = [
    re_path(r'random/', killer_views.RandomKillerView.as_view({'post': 'random'}), name='random-killer'),
    re_path('', killer_views.KillerView.as_view({'get': 'retrieve'}), name='killer'),
]