from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='search-index'),
    path('<int:id', views.get_prop_by_id, name='prop-details')
]