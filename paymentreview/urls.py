from django.urls import path
from . import views
from payment import views

urlpatterns = [
    path('<int:id>', views.paymentReview, name='paymentreview-index'),
]