from django.urls import path
from .views import *
urlpatterns=[
path('index/',index),
    path('login/',login),
    path('register/',register),
    path('profile/',profile),
    path('logout/',logout),
    path('about/',about),
    path('footer/',footer),
    path('addjob/<int:id>',addjob),
    path('contacts/',contact),
    path('vacancydis/',vacancydis),
    path('editvacancy/<int:id>',editvacancy),
    path('deletevac/<int:id>',vacancydel),
    path('ureg/',ureg),
    path('ulog/',ulogin.as_view(),name='ulog'),
    path('comdis/',comdis),
    path('userpro/',userprofile,name='userpro'),
    path('addpro/',addprofiledetails.as_view(),name='addpro'),
    path('viewvac/',viewvac.as_view(),name='viewvac'),
    path('viewpro/',ureg)


]