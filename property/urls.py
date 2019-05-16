from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='property-index'),
    path('<int:id', get_prop_by_id, name='prop-details')
]