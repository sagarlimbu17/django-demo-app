
from django.urls import path

from basic_app.views import index, register
from user_registration import settings
from .views import user_login
app_name = 'basic_app'
urlpatterns = [
    path('', index,name='index'),
    path('register/', register, name='register'),
    path('user_login/', user_login, name='user_login'),
]
