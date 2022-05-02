from lib2to3.pgen2 import token
from random import randint, random
from django.shortcuts import render
from .models import Blogpost, letsblog
from django.views.generic import ListView

def index(request):
    blogs = Blogpost.objects.all()
    limit_max=20
    n=len(blogs)
    params={'blogs':blogs,'strlen':n,'lim':limit_max}
    return render(request,"blogapp/index.html",params)


def contact(request):
    return render(request,"blogapp/contact.html")

def feed(request):
    name=request.GET.get('name')
    qstn=request.GET.get('querry')
    mail=request.GET.get('email')
    phone=request.GET.get('phone')
    tokenid=100
    params={'username':name,'question':qstn,'mail':mail,'contact_number':phone,'tokenid':tokenid}
    return render(request,"blogapp/feedgone.html",params)


def about(request):
    return render(request,"blogapp/about.html")

def donation(request):
    return render(request,"blogapp/donation.html")

def faqs(request):
    return render(request,"blogapp/faqs.html")

def login(request):
    return render(request,"blogapp/login.html")

def signup(request):
    return render(request,"blogapp/signup.html")

def aboutblogs(request):
    return render(request,"blogapp/aboutblogs.html")

def topbloggers(request):
    return render(request,"blogapp/topbloggers.html")

def postoftheday(request):
    blogs = letsblog.objects.all()
    limit_max=20
    n=len(blogs)
    params={'blogs':blogs,'strlen':n,'lim':limit_max}
    return render(request,"blogapp/postoftheday.html",params)

def blogview(request,myid):
    blog = letsblog.objects.filter(letsblog_id=myid)
    return render ( request, 'blogapp/blogview.html',{'blog':blog[0] })

def blogbeforeview(request,myid):
    blog=Blogpost.objects.filter(id=myid)
    return render ( request, 'blogapp/blogbeforeviewview.html',{ 'blog':blog[0] })
