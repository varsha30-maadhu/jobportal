from django import forms
from django.contrib.auth.models import User
from .models import *


class regform(forms.Form):
    cname = forms.CharField(max_length=25)
    address = forms.CharField(max_length=100)
    email = forms.EmailField()
    phn = forms.IntegerField()
    password = forms.CharField(max_length=20)
    cpassword = forms.CharField(max_length=20)
class logform(forms.Form):
    email=forms.CharField(max_length=25)
    password=forms.CharField(max_length=20)
class addform(forms.Form):
    cname = forms.CharField(max_length=50)
    email = forms.EmailField()
    title = forms.CharField(max_length=35)

    jtype = forms.CharField(max_length=100)
    worktype = forms.CharField(max_length=100)
    exp = forms.CharField(max_length=20)
    qua = forms.CharField(max_length=100)
class uregform(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","email","password","first_name","last_name"]
class ulog(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=25)
class profileform(forms.ModelForm):
    class Meta:
        model=addprofile
        fields='__all__'

