from django.shortcuts import render,redirect
from login.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from login.models import *
from django.contrib.auth.models import User
from django.views import generic

from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request,'login/index.html')


def register(request):
    user_form=UserForm()
    registered= False
    if request.method=="POST":

        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if (user_form.is_valid() and profile_form.is_valid()):
            user=user_form.save()
            user.set_password(user.password)
            user.save()


            profile=profile_form.save(commit=False)
            profile.user=user #onetoone relation
            if profile_pic in request.FILES:
                profile.profile_pic= request.FILES['profile_pic']

            profile.save()

            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    return render(request,'login/registration.html',{'username':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    print("login page attempt")
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)


        user=authenticate(username=username,password=password)

        if user is not None:
            #if user.is_active():
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            #else:
                #return HttpResponse("Account Not Active")
        else:
            print("false login")
            return HttpResponseRedirect(reverse('index'))
    else:
        print("render part ran successfully")
        return render(request,'login/userlogin.html')


@login_required
def user_logout(request):
    print("logout")
    logout(request)
    return HttpResponseRedirect(reverse('index'))



@login_required
def dashboard(request):


#     if request.method=="POST":
#          dash_form=UserStockDisplayForm(data=request.POST)
#          if (dash_form.is_valid()):
#              print(request.user.username)
#              #dash_form.TeamId=request.user.username
#              dash_form.author=UserProfileInfo.objects.get(user=request.user)
#              dash_form.save()
#
      user_dashdata=UserStockDisplay.objects.all()
      UserStockDisplayDic={'dashdata':user_dashdata}
      return render(request,'login/dashboard.html',{'dashdata':user_dashdata})

class UserStockDisplayCreateView(LoginRequiredMixin,generic.CreateView):
	model=UserStockDisplay
	form_class=UserStockDisplayForm
	template_name='login/userstockcreate.html'

	def form_valid(self,form):
		userStockDisplay=form.save(commit=False)
        # form.instance.author = self.request.user
		userStockDisplay.author=self.request.user
		userStockDisplay.save()
		return redirect('login:dashboard')





@login_required
def news(request):
    news_list=News.objects.all()
    NewsDic={'news':news_list}
    return render(request,'login/news.html',context=NewsDic)


@login_required
def stockprice(request):
    stock_list=Stock.objects.all()
    StockDic={'stocks':stock_list}
    return render(request,'login/stockprice.html',context=StockDic)



class brokerdashboard(generic.ListView):
    template_name='login/brokerdashboard.html'
    context_object_name='brokerdashdata'

    def get_queryset(self):
        return UserStockDisplay.objects.all()


class deleteUserStockDisplay(generic.DeleteView):
    print("deleteblock")
    template_name='login/dashboard.html'
    model=UserStockDisplay
    success_url =reverse_lazy('login:dashboard')
