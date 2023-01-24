from django.urls import path
from .views import *
urlpatterns=[
path('index/',index),
    path('register/',register),
    path('login/',login),
    path('reg/',reg),
    path('display/',display),
    path('editdis/<int:id>',editdis),
    path('deldisplay/<int:id>',deldisplay)
]