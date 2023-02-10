from django.contrib import admin
from .models import Account, Group, Comment
# Register your models here.
admin.site.register(Account) 
admin.site.register(Group) 
admin.site.register(Comment) 