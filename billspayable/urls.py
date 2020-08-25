"""billspayable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from billspayable.api import user_viewset
from billspayable.api import staff_viewset
from django.contrib import admin
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()

# Customer Apis
router.register(r'invoice', user_viewset.UserViewset)
# Staff Apis
router.register(r'staff', staff_viewset.StaffViewset)

urlpatterns = router.urls

