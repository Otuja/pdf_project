from django.contrib import admin
from django.urls import path

from .views import index, detail, signup, pdf_list, new, delete, edit, custom_logout, subscribe

# for login
from django.contrib.auth import views as auth_views
from .forms import LoginForm 

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:id>/', detail, name='detail'),
    path('<int:id>/delete/', delete, name='delete'),
    path('<int:id>/edit/', edit, name='edit'),
    path('files/', pdf_list, name='pdf-list'),
    path('new/', new, name='new'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout', custom_logout, name='logout'),
    path('subscribe/', subscribe, name='subscribe'),    
]
