"""castleApt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.castleApt, name='castleApt')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='castleApt')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('signup/', include('signup.urls')),
    path('contacts/', include('contacts.urls')),
    path('aboutus/', include('aboutus.urls')),
    # path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('logout', include('logout.urls')),
    path('property/', include('property.urls')),
    path('contactus/', include('contactus.urls')),
    path('search/', include('search.urls')),
    path('payment/', include('payment.urls')),
    path('sell/', include('sell.urls')),
    path('profile/', include('editprofile.urls')),
    path('paymentreview/', include('paymentreview.urls')),
]
