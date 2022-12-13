"""bike URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bikeApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('reg',views.reg),
    path('login',views.login_),
    path('spec',views.spec),
    path('color',views.color),
    path('about',views.about),
    path('images',views.images),
    path('adminlogin',views.adminlogin),
    path('customerlogin',views.customerlogin),
    path('customer',views.customer),
    path('addvehicle',views.addvehicle),
    path('stockupdation',views.stockupdation),
    path('bookingdetails',views.bookingdetails),
    path('viewvehicle',views.viewvehicle),
    path('updateVeh',views.updateVeh),
    path('profile',views.profile),
    path('vehicle',views.vehicle),
    path('booking',views.booking),
    path('approvereject',views.approvereject),
    path('logout',views.logout_),
    path('aprej',views.aprej),
    path('status',views.status),
    path('specc',views.specc),
    path('colorc',views.colorc),
    path('imagesc',views.imagesc),
    path('aboutc',views.aboutc),
    
]
