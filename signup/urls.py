from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='signup-index'),
    # path('<int:id>', views.getUser, name='getUser-index'),
    path('', views.createUser, name='createUser'),
    path('', views.index, name='signup-index'),
    #path('create_user', views.createUser, name='createUser'),
]