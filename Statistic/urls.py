from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home, name='home_url'),
    path('Регистрация', USER_SIGN_UP, name='sign_up_url'),
    path('Вход', USER_SIGN_IN, name='sign_in_url'),
    path('Выход', USER_SIGN_OUT, name='sign_out_url'),
    path('Отправка_письма', SEND_EMAIL.as_view(), name='send_email_url'),
    path('Красовок', card, name='card_url'),
]
