from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', LogoutView.as_view(next_page='login.html'), name='logout'),
]