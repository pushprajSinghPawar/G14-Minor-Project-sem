from xml.parsers.expat import model
from django.db import models

# Create your models here.

class Blogpost(models.Model):
    Blogpost_id=models.AutoField
    Blogpost_title=models.CharField(max_length=50)
    Blogpost_blog=models.CharField(max_length=400)
    Blogpost_date=models.DateField()
    