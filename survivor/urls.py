from django.urls import re_path
from . import views as survivor_views

urlpatterns = [
    re_path(r'^random/$', survivor_views.RandomSurvivorView.as_view({'post': 'random'}), name='random-survivor'),
    re_path(r'^(?P<pk>\d+)/$', survivor_views.SurvivorView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='survivor-detail'),
    re_path(r'^$', survivor_views.SurvivorView.as_view({'get': 'list', 'post': 'create'}), name='survivor-list'),
]
