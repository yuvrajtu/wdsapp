"""wdsapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from login import views


urlpatterns = [
    path('',views.index,name="index"),
    path('login/',include('login.urls')),
    path('admin/', admin.site.urls),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('news/',views.News,name="news"),
    path('brokerdashboard/',views.brokerdashboard.as_view(),name="brokerdashboard"),
    path('dashboard/<int:pk>/',views.deleteUserStockDisplay.as_view(),name="UserStockDisplaydelete"),
    path('dashboard/create', views.UserStockDisplayCreateView.as_view(), name='stock_create'),


]
