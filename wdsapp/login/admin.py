from django.contrib import admin
from login.models import UserProfileInfo,Stock,UserStockDisplay,News
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(Stock)
admin.site.register(UserStockDisplay)
admin.site.register(News)
