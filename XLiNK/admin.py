from django.contrib import admin
from .models import Account, Group, Comment, Category
# Register your models here.
admin.site.register(Account) 
admin.site.register(Comment) 
admin.site.register(Category)
admin.site.register(Group)