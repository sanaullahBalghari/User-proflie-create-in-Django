from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import *
from django.contrib import messages
from .forms import profileForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login/')
def index_view(request):

    return render(request, 'profileapp/home.html')
@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        form = profileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, your profile is updated.')
            return redirect('/')
    else:
        form = profileForm(instance=request.user.profile)

    # Ensure context is always defined
    context = {
        'form': form
    }

    return render(request, 'profileapp/profile.html', context)

def login_user(request):
    if request.method== 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'{username}, You are logged in')
          
            return redirect('/')
        else:
            messages.info(request, 'invalid username or password!')
            return redirect('login_user')
    return render(request, 'profileapp/login_page.html')

def register_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm-password')
        if confirm_password==password:
            user=User.objects.create(username=username,email=email)
            user.set_password(password)
            user.save()
            return redirect('login_user')
        else:
            messages.error(request ,'Password are not same please Try again!')
            return redirect('register_user')
        
    return render(request, 'profileapp/register_page.html')

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.info(request,'You are logout successfully')
    return redirect('logout_user')