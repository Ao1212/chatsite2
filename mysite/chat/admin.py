from django.contrib import admin
from .models import ChatHistory, Group, GroupMember

# Register your models here.

admin.site.register(ChatHistory)
admin.site.register(Group)
admin.site.register(GroupMember)
