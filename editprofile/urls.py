from django.urls import path
from . import views
from editprofile.views import UpdateProfile

urlpatterns = [
    path('', views.profile, name='editprofile-index'),
]