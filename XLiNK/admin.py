from django.contrib import admin
from .models import Account, Group, Comment, Category, FollowersCount
# Register your models here.
admin.site.register(Account) 
admin.site.register(Comment) 
admin.site.register(Category)
admin.site.register(Group)
admin.site.register(FollowersCount)