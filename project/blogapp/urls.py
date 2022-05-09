from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
path('', views.index, name="blog"),
path('login',views.login,name="login"),
path('signup',views.signup,name="signup"),
path('faqs',views.faqs,name="faqs"),
path('donations',views.donation,name="donation"),
path('about',views.about,name="about"),
path('aboutblogs',views.aboutblogs,name="aboutblogs"),
path('topbloggers',views.topbloggers,name="topbbloggers"),
path('postoftheday',views.postoftheday,name="potd"),
path('blogview/<int:myid>',views.blogview,name="blogview"),
path('blogbeforeview/<int:myid>',views.blogbeforeview,name="blogbeforeview"),
path('contact',views.contact_view,name="contact"),
path('search',views.search,name="search"),
path('feed',views.feed,name="feed"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)