from django import forms
from django.contrib.auth.models import User
from login.models import *
from django.http import HttpResponseRedirect,HttpResponse

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username','email','password')


class UserStockDisplayForm(forms.ModelForm):
    class Meta():
        model=UserStockDisplay
        fields=['StockName','NumberOfStock','SellingPrice']
