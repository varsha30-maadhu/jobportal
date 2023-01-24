from django.db import models

# Create your models here.
class regmodel(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    image=models.FileField(upload_to='sample_app/static')
    password=models.CharField(max_length=25)
