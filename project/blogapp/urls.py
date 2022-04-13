from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name="blog"),
path('login',views.login,name="login"),
path('signup',views.signup,name="signup"),
path('faqs',views.faqs,name="faqs"),
path('donations',views.donation,name="donation"),
path('about',views.about,name="about"),
]