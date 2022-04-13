from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request,"blogapp/index.html")

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
    return render(request,"blogapp/postoftheday.html")

