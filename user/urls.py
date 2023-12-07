from django.urls import re_path
from . import views as user_views

urlpatterns = [
    re_path('login/', user_views.LoginView.as_view(), name='login'),
    re_path(r'register/', user_views.RegisteredUserViewSet.as_view({'post': 'create'}), name='register'),
    re_path(r'check-auth/', user_views.check_auth, name='check-auth'),

]
