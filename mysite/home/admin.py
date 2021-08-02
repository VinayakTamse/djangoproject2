from django.contrib import admin
from .models import ExtraField, Member, UserMember, AgentMode

# Register your models here.
admin.site.register(ExtraField)
admin.site.register([Member, UserMember, AgentMode])