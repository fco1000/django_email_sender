from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import login,logout,authenticate
from .models import user
from .forms import UserSignUpForm,UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import UpdateView
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def userCreationView(request):
    form = UserSignUpForm()
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        User = user.objects.create_user(
            username=username,
            email=email
        )
        login(request,User)
        send_mail(  subject = 'welcome to Test Email',
                    message = f'Hi {User.username}, thank you for registering in FCO1000.',
                    from_email = settings.EMAIL_HOST_USER,
                    recipient_list = [User.email, ],
                    fail_silently=False)
        message = f'{User.username}\'s Account creation successful.Please verify your email'
        messages.success(request, message)
        return redirect('home')        
    else:
        return render(request, 'users/register_user.html', {'form': form})
    
        

class userChangeView(View):
    def get(self,request):
        form= UserChangeForm()
        return render(request, 'users/register_user.html', {'form': form})
        
    def post(self,request):
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'users/update_user.html', {'form': form}) 
    
class userLogoutView(LoginRequiredMixin,LogoutView):
    template_name = 'users/logout_user.html'
    
    def get_success_url(self):
        return reverse('home') 

    
class userLoginView(LoginView):
    template_name = 'users/login_user.html'
    
    def get_success_url(self):
        return reverse('home') 
       
def showUserView(request):
    current_user = request.user
    return render(request,'users/demo.html',{'user':current_user})