from django.db import models

# Create your models here.
class regmodel(models.Model):
    cname=models.CharField(max_length=25)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phn=models.IntegerField()
    password=models.CharField(max_length=20)
class addmodel(models.Model):
    catchoice = [

        ('parttime','parttime'),
        ('Full-time','Full-time'),

    ]
    cho=[

        ('hybrid','hybrid'),
        ('remote','remote'),
    ]
    choice=[
        ('0-1','0-1'),
        ('1-2','1-2'),
        ('2-3','2-3'),
        ('3-4','3-4'),
        ('4-5','4-5'),
        ('5-6','5-6'),
        ('6-7','6-7'),
        ('7-8','7-8'),
        ('8-9','8-9'),
        ('9-10','9-10'),
    ]

    cname=models.CharField(max_length=50)
    email=models.EmailField()
    title=models.CharField(max_length=35)

    jtype=models.CharField(max_length=100,choices=catchoice)
    worktype=models.CharField(max_length=100,choices=cho)
    exp=models.CharField(max_length=20,choices=choice)
    qua=models.CharField(max_length=100)
class addprofile(models.Model):
    image=models.ImageField(upload_to='jobapp/static')
    fname=models.CharField(max_length=50)
    email=models.EmailField()
    resume=models.FileField(upload_to='jobapp/static')
    eduqua=models.CharField(max_length=50)
    exp=models.CharField( max_length=60)
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
