from django.urls import path

from .views import employee

urlpatterns = [
    path('add_employee/', employee, name='employee')
]
