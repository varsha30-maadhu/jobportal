from django import forms
class regform(forms.Form):
    name=forms.CharField(max_length=25)
    email=forms.EmailField()
    image=forms.FileField()
    password=forms.CharField(max_length=25)
    cpass=forms.CharField(max_length=25)
