from django.urls import path
from .views import home, login_view, register, user_exit

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('exit/', user_exit, name='exit'),
]