from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from .forms import *
from .models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        a = logform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            b = regmodel.objects.all()  # companyname ,address
            for i in b:
                cmp = i.cname
                id = i.id
                if i.email == em and i.password == ps:
                    return render(request, 'profile.html', {'cmp': cmp, 'id': id})  # wipro #1
            else:
                return HttpResponse('login failed')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        a = regform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data["cname"]
            add = a.cleaned_data["address"]
            em = a.cleaned_data["email"]
            ph = a.cleaned_data["phn"]
            ps = a.cleaned_data["password"]
            cp = a.cleaned_data["cpassword"]
            if ps == cp:
                b = regmodel(cname=nm, address=add, email=em, phn=ph, password=ps)
                b.save()
                return redirect(login)
            else:
                return HttpResponse('incorrect password')
        else:
            return HttpResponse('registration failed')
    else:
        return render(request, 'register.html')


def profile(request):
    return render(request, 'profile.html')


def logout(request):
    return redirect(profile)


def about(request):
    return render(request, 'about.html')


def footer(request):
    return render(request, 'footer2.html')


def addjob(request, id):
    b = regmodel.objects.get(id=id)
    cm = b.cname
    em = b.email
    if request.method == 'POST':
        a = addform(request.POST)

        if a.is_valid():
            nm = a.cleaned_data["cname"]
            em = a.cleaned_data["email"]
            ti = a.cleaned_data["title"]
            jt = a.cleaned_data["jtype"]
            wt = a.cleaned_data["worktype"]
            ex = a.cleaned_data["exp"]
            qu = a.cleaned_data["qua"]
            b = addmodel(cname=nm, email=em, title=ti, jtype=jt, worktype=wt, exp=ex, qua=qu)
            b.save()
            return redirect(vacancydis)

        else:
            return HttpResponse('upload failed')
    else:
        return render(request, 'addjob.html', {'cm': cm, 'em': em})


def contact(request):
    return render(request, 'contacts.html')


def vacancydis(request):
    x = addmodel.objects.all()
    y = regmodel.objects.all()
    return render(request, 'vacancydis.html', {'x': x, 'y': y})


def editvacancy(request, id):
    a = addmodel.objects.get(id=id)
    if request.method == 'POST':
        a.cname = request.POST.get('cname')
        a.email = request.POST.get('email')
        a.title = request.POST.get('title')
        a.jtype = request.POST.get('jtype')
        a.worktype = request.POST.get('worktype')
        a.exp = request.POST.get('exp')
        a.qua = request.POST.get('qua')
        a.save()
        return redirect(vacancydis)
    return render(request, 'editvacancy.html', {'a': a})


def vacancydel(request, id):
    a = addmodel.objects.get(id=id)
    a.delete()
    return redirect(vacancydis)


def ureg(request):
    if request.method == 'POST':
        a = uregform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data["first_name"]
            add = a.cleaned_data["last_name"]
            em = a.cleaned_data["email"]
            ph = a.cleaned_data["username"]
            ps = a.cleaned_data["password"]
            b = User(first_name=nm, last_name=add, email=em, username=ph, password=ps)
            for i in b:
                fname=i.first_name
                lname=i.last_name
                eam=i.email
                return render(request,'viewprofile.html',{'fname':fname,'lname':lname,'eam':eam})
            b.save()
            return redirect(login)

        else:
            return HttpResponse('registration failed')

    else:
        return render(request, 'userregister.html')


# class userreg(generic.CreateView):
#     form_class = uregform
#     template_name = 'userregister.html'
#     success_url = reverse_lazy('ulog')

# def get(self,request):
#     a=User.objects.all()
#     for i in a:
#
#         fname=i.first_name
#         lname=i.last_name
#         em=i.email

#     return render(request,'viewprofile.html',{'fname':fname,'lname':lname,'em':em})
# another method
#     def get(self,request,id):
#         b = User.objects.get(id=id)
#         fname = b.first_name
#         lname=b.last_name
#         eam = b.email
#         return render(request,'viewprofile.html',{'fname':fname,'lname':lname,'eam':eam})
#         if request.method=='POST':
#             for i in a:
#                 fname=request.POST.get('first_name')
#                 lname=request.POST.get('last_name')
#                 eam=request.POST.get('email')
#                 return render(request,'viewprofile.html',{'fname':fname,'lname':lname,'eam':eam})


class ulogin(generic.View):
    form_class = ulog
    template_name = 'ulogin.html'
    success_url = reverse_lazy('userpro')

    def get(self, request):
        a = ulog
        return render(request, 'ulogin.html')

    def post(self, request):
        if request.method == 'POST':
            a = ulog(request.POST)
            if a.is_valid():
                em = a.cleaned_data['email']
                ps = a.cleaned_data['password']
                b = User.objects.all()
                for i in b:

                    if i.email == em and i.password == ps:
                        return redirect(userprofile)

                else:
                    return HttpResponse('login failed')


def comdis(request):
    x = regmodel.objects.all()
    return render(request, 'companydis.html', {'a': x})


def userprofile(request):
    return render(request, 'userprofile.html')


class addprofiledetails(generic.CreateView):
    form_class = profileform
    template_name = 'addprofile.html'
    success_url = reverse_lazy('userpro')
    # def get(self,request):
    #     a=addprofile.objects.all()
    #     for i in a:
    #         eq=i.eduqua
    #         return render(request,'viewprofile.html',{'eq':eq})


class viewvac(generic.ListView):
    model = addmodel
    template_name = 'viewvacncy.html'

    def get(self, request):
        a = self.model.objects.all()
        return render(request, self.template_name, {'a': a})
# class viewpro(generic.ListView):
#     model=addprofile
#     template_name = 'viewprofile.html'
#
#     def get(self, request):
#         a = self.model.objects.all()
#         image = []
#         fnam = []
#         em=[]
#         re=[]
#         edu=[]
#         ex=[]
#         add=[]
#         ph=[]
#         # id1 = []
#         for i in a:
#             # id = i.id
#             # id1.append(id)
#             im = str(i.image).split('/')[-1]
#             image.append(im)
#             nm = i.fname
#             fnam.append(nm)
#             eam=i.email
#             em.append(eam)
#             resu=str(i.resume).split('/')[-1]
#             re.append(resu)
#             ed=i.eduqua
#             edu.append(ed)
#             e=i.exp
#             ex.append(e)
#             ad=i.address
#             add.append(ad)
#             phn=i.phone
#             ph.append(phn)
#
#         mylist = zip(image, fnam,em,re,edu,ex,add,ph)
# #         return render(request, self.template_name, {'a': mylist})
# def viewpro(request,id):
#     a=addprofile.objects.get(id=id)
#     fnam=a.fname
#     return render(request,'viewprofile.html',{'fname':fnam})
