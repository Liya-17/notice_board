from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registerPage, name='register'), 
    path('login/',views.loginPage, name='login'), 
    path('logout/',views.logoutPage, name='logout'),
    path('', views.notice_list, name='notice_list'),
    path('create/', views.notice_create, name='notice_create'),
    path('delete/<int:pk>/', views.notice_delete, name='notice_delete'),
    path('home/', views.homepage, name='homepage'), 
]
