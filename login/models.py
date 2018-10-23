from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

class Stock(models.Model):
    StockName = models.CharField(blank=True, max_length=100)
    CurrentPrice = models.FloatField(null=True,blank=True)
    def __str__(self):
        return self.StockName

class UserStockDisplay(models.Model):
    #TeamId=models.CharField(blank=True, max_length=100)
    author=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    StockName = models.ForeignKey(Stock,on_delete=models.CASCADE)
    NumberOfStock = models.IntegerField(blank=False, null=False)
    SellingPrice = models.FloatField(blank=False,null=False)

class News(models.Model):
    Id = models.AutoField(primary_key=True)
    StockNews = models.TextField(blank=True)
