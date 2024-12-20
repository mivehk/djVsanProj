from django.urls import path
from django.contrib.auth import views as defaultViews
from . import views


urlpatterns = [
    path('', defaultViews.LoginView.as_view(template_name='registration/login.html')),
    path('register/', views.register, name='register'),  
    path('login/', defaultViews.LoginView.as_view(template_name='registration/login.html'), name='login'), 
    path('logout/', defaultViews.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),  
    path('dashboard/', views.dashboard, name='dashboard'), 
]