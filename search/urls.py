from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='search-index'),
    # path('sort<str:order>', views.orderBy, name='search-order'),
]