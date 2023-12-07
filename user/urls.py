from django.urls import re_path
from . import views as user_views

urlpatterns = [
    # re_path('login/', user_views.login_view.as_view(), name='login'),
    re_path(r'register/', user_views.RegisteredUserViewSet.as_view({'post': 'create'}), name='register'),

]
