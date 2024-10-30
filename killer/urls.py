from django.urls import re_path
from . import views as killer_views

urlpatterns = [
    re_path(r'^random$', killer_views.RandomKillerView.as_view({'get': 'random'}), name='killer-random'),
    re_path(r'^(?P<pk>\d+)/$', killer_views.KillerView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='killer-detail'),
    re_path(r'^$', killer_views.KillerView.as_view({'get': 'list', 'post': 'create'}), name='killer-list'),
]
