from django.shortcuts import render,redirect
import os
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    return render(request,'registeration.html')
def login(request):
    return render(request,'login.html')
def reg(request):
    if request.method=='POST':
        a=regform(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data['name']
            em = a.cleaned_data['email']
            im = a.cleaned_data['image']
            ps = a.cleaned_data['password']
            cps = a.cleaned_data['cpass']
            if(ps==cps):
                f=regmodel(name=nm,email=em,image=im,password=ps)
                f.save()
                return HttpResponse('new product added')
            else:
                return HttpResponse('incorrect password')
        else:
            return HttpResponse('failed')
    else:
        return render(request,'register.html')
def display(request):
    x=regmodel.objects.all()
    nm=[]
    em=[]
    img=[]
    ps=[]
    id=[]
    for i in x:
        id1=i.id
        id.append(id1)
        nam=i.name
        nm.append(nam)
        eam=i.email
        em.append(eam)
        im=i.image
        img.append(str(im).split('/')[-1])
        pas=i.password
        ps.append(pas)
        mylist=zip(nm,em,img,ps,id)
        return render(request,'display.html',{'a':mylist})
def editdis(request,id):
    a=regmodel.objects.get(id=id)
    image=str(a.image).split('/')[-1]
    if request.method=='POST':
        a.name=request.POST.get('name')
        a.email = request.POST.get('email')

        a.password = request.POST.get('password')
        if len(request.FILES)!=0:
            if len(a.image)>0:
                os.remove(a.image.path)
            a.image=request.FILES.get(image)
            a.save()
            return redirect(display)
    return render(request,'editdis.html',{'a':a,'image':image})
def deldisplay(request,id):
    a=regmodel.objects.get(id=id)
    if len(a.image)>0:
        os.remove(a.image.path)
    a.delete()
    return redirect(display)














