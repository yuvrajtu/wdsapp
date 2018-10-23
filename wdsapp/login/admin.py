from django.contrib import admin
from login.models import UserProfile,Stock,UserStockDisplay,News
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Stock)
admin.site.register(UserStockDisplay)
admin.site.register(News)
