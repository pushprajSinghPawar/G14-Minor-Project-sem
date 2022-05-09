from distutils.command.upload import upload
import email
from email.policy import default
from xml.parsers.expat import model
from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Blogpost(models.Model):
    Blogpost_id=models.AutoField
    # likes=models.IntegerField('')
    Blogpost_title=models.CharField(max_length=50,default='title<xyz>')
    Blogpost_desc=models.TextField(max_length=45,default="this is the description of blog")
    Blogpost_blog=models.TextField(max_length=5400,default='blog content test  <xyz>')
    strcat =  (
       ('education', ('educational')),
       ('lifestyle', ('lifestyle')),
       ('sports',    ('sports')),
       ('diy' , ('diy')),
       ('fashion',('fashion')),
       ('entertainment',('entertainment')),
       ('science',('science')),
       ('health', ('health')),
       ('personal', ('personal')),
       ('others' , ('others')),
    )
    Blogpost_category1=models.CharField(max_length=50,choices=strcat,default='others')
    Blogpost_date=models.DateField()
    Blogpost_picture1=models.ImageField(upload_to="blogapp/images",default="blogapp/logo.png")
    tags  = TaggableManager()
    def __str__(self):
        return self.Blogpost_title

class letsblog(models.Model):
    letsblog_id=models.IntegerField(primary_key=True)
    letsblog_title=models.CharField(max_length=40)
    letsblog_desc=models.TextField(max_length=40,default="this is the description of blog")
    letsblog_blog=models.TextField(max_length=700)
    blogCategories =  (
       ('education', ('educational')),
       ('lifestyle', ('lifestyle')),
       ('sports',    ('sports')),
       ('diy' , ('diy')),
       ('fashion',('fashion')),
       ('entertainment',('entertainment')),
       ('science',('science')),
       ('health', ('health')),
       ('personal', ('personal')),
       ('others' , ('others')),
    )
    letsblog_category1=models.CharField(max_length=50,choices=blogCategories,default='others')
    letsblog_date=models.DateField()
    letsblog_picture1=models.ImageField(upload_to="blogapp/images")
    
    def __str__(self):
        return self.letsblog_title


class contact(models.Model):
    name=models.CharField(default='xxyyzz', max_length=100)
    phonenum=models.IntegerField(default='9399237742')
    email=models.EmailField(null=True,blank=True)
    querry=models.CharField(default='no querry' ,max_length=200)
    def __str__(self):
        return self.name

    