from django.shortcuts import render, redirect

# Create your views here.
from .models import Notice
from .forms import NoticeForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required 
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_protect

def registerPage(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.success(request, "Password does not follow the rules")
    
    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username, password)
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.success(request, "Username or Password is incorrect")
                
        context = {}
        return render(request, 'login.html', context)
    
@login_required(login_url='login') 
@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
def logoutPage(request): 
    logout(request) 
    return redirect('login')

@login_required(login_url='login') 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def notice_list(request):
    notices = Notice.objects.all().order_by('-created_at')
    return render(request, 'notices/notice_list.html', {'notices': notices})

@login_required(login_url='login') 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def notice_create(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            form.save()
            return redirect('notice_list')
    else:
        form = NoticeForm()
    return render(request, 'notices/notice_form.html', {'form': form})

@login_required(login_url='login') 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def notice_delete(request, pk):
    notice = Notice.objects.get(pk=pk)
    notice.delete()
    return redirect('notice_list')

@login_required(login_url='login') 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def homepage(request):
    return render(request, 'notices/homepage.html')