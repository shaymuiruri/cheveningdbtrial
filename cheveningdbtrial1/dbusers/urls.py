from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

app_name = 'dbusers'


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='dbusers/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='dbusers/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
]
