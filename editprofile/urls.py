from django.urls import path
from . import views
from editprofile.views import UpdateProfile

urlpatterns = [
    path('', views.index, name='editprofile-index'),
]