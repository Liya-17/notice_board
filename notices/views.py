from django.shortcuts import render, redirect, get_object_or_404

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
from django.utils import timezone
from django.db.models import Q
from .models import Notice, Category, Tag 

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

# views.py
@login_required(login_url='login') 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def notice_list(request):
    category_filter = request.GET.getlist('category')
    tag_filter = request.GET.getlist('tag')
    # Filter notices to only show active (non-expired) ones
    notices = Notice.objects.filter(
        Q(expiry_date__isnull=True) | Q(expiry_date__gt=timezone.now())
    ).order_by('-created_at')
    
    if category_filter:
        notices = notices.filter(categories__in=category_filter).distinct()
    
    if tag_filter:
        notices = notices.filter(tags__in=tag_filter).distinct()

    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'notices/notice_list.html', {
        'notices': notices,
        'categories': categories,
        'tags': tags,
        'category_filter': category_filter,
        'tag_filter': tag_filter
    })
    


# views.py
@login_required(login_url='login') 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def notice_create(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('notice_list')
    else:
        form = NoticeForm()
    return render(request, 'notices/notice_form.html', {'form': form})


@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def notice_edit(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES, instance=notice)
        if form.is_valid():
            form.save()
            return redirect('notice_list')
    else:
        form = NoticeForm(instance=notice)
    return render(request, 'notices/notice_form.html', {'form': form, 'notice': notice})

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