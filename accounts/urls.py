from django.urls import path
from . import views

upp_name = 'accounts'

urlpatterns = [
    path('', views.signup, name='signup'),
]