from distutils.command.upload import upload
from xml.parsers.expat import model
from django.db import models

# Create your models here.

class Blogpost(models.Model):
    Blogpost_id=models.AutoField
    Blogpost_title=models.CharField(max_length=50)
    Blogpost_blog=models.CharField(max_length=400)
    Blogpost_category1=models.CharField(max_length=50,default="")
    Blogpost_category2=models.CharField(max_length=50,default="")
    Blogpost_category3=models.CharField(max_length=50,default="")
    Blogpost_category4=models.CharField(max_length=50,default="")
    Blogpost_category5=models.CharField(max_length=50,default="")
    Blogpost_category6=models.CharField(max_length=50,default="")
    Blogpost_date=models.DateField()
    Blogpost_picture1=models.ImageField(upload_to="blogapp/images",default="")
    
    def __str__(self):
        return self.Blogpost_title