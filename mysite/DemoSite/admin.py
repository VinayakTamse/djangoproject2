from django.contrib import admin
from .models import DemoSite, DemoUser

# Register your models here.

admin.site.register((DemoSite, DemoUser))
