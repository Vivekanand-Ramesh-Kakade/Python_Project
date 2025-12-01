from django.urls import path
from .views import create_user_and_send_temp_password

urlpatterns = [
    path('create-temp-user/', create_user_and_send_temp_password, name='create_temp_user'),
]
