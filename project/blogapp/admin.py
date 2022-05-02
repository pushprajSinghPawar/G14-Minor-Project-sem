from django.contrib import admin

# Register your models here.

from .models import Blogpost, letsblog 

admin.site.register(Blogpost)

admin.site.register(letsblog)
