from django.contrib import admin

# Register your models here.

from .models import Blogpost, letsblog , contact

admin.site.register(Blogpost)

admin.site.register(letsblog)

admin.site.register(contact)
