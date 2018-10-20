from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

class Stock(models.Model):
    StockName = models.CharField(blank=True, max_length=100)
    CurrentPrice = models.FloatField(null=True,blank=True)

class UserStockDisplay(models.Model):
    StockName = models.CharField(blank=False,max_length=100)
    NumberOfStock = models.IntegerField(blank=False, null=False)
    SellingPrice = models.FloatField(blank=False,null=False)

class News(models.Model):
    Id = models.AutoField(primary_key=True)
    StockNews = models.TextField(blank=True)

    def __str__(self):
        return self.name
