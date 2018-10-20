from django.conf.urls import url
from django.urls import path,include
from login import views

app_name='login'

urlpatterns=[

path('register/',views.register,name='register'),
path('userlogin/',views.user_login,name='userlogin'),
path('dashboard/',views.dashboard,name='dashboard'),
path('user_logout/',views.user_logout,name='user_logout'),
path('news/',views.news,name='news'),
path('stockprice/',views.stockprice,name='stockprice'),
]
