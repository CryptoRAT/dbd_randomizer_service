from django.urls import re_path
from . import views as survivor_views

urlpatterns = [
    # the path for url to get a random survivor as a post call

    re_path('random/', survivor_views.RandomSurvivorView.as_view({'post': 'random'}), name='random-survivor'),
    re_path('', survivor_views.SurvivorView.as_view({'get': 'retrieve'}), name='survivor'),
]




