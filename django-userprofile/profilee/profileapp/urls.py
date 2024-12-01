from django.urls import path
from .views import*

urlpatterns = [
    path('', index_view, name='home'),
    path('profile/', profile, name='profile'),
    path('login/', login_user, name='login_user'),
    path('register_user/', register_user, name='register_user'),
    path('logout_user/', logout_user, name='logout_user'),
   
   
]