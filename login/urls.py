from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login-index'),
    # path('', LoginView.as_view(template_name='Log_in/login.html'), name='login-index'),
]