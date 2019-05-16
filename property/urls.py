from django.urls import path
from . import views
from search import views

urlpatterns = [
    path('<int:id>', views.get_prop_by_id, name='property-index'),

]