from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>', login_required(views.UserProfileView.as_view()), name='profile'), # Параметр pk нужен для UpdateView
    path('logout', views.logout, name='logout'),
]
