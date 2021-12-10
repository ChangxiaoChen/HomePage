"""HomePage URL Configuration

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
from django.conf import settings
from django.urls import path, re_path,include

from . import views

''' SimpleRouter用于注册路由 '''
from rest_framework.routers import SimpleRouter


urlpatterns = [
    path('get_email/',views.EmailViewSet.as_view({'get': 'get_email'})),
    path('reg_codes/',views.EmailViewSet.as_view({'get': 'reg_codes'})),
    path('login_codes/',views.EmailViewSet.as_view({'get': 'login_codes'})),
    path('pwd_codes/',views.EmailViewSet.as_view({'get': 'pwd_codes'})),
    path('reg/',views.RegisterViewSet.as_view({'post': 'reg'})),
    path('login/',views.LoginViewSet.as_view({'post': 'login'})),
    path('code_login/',views.LoginViewSet.as_view({'post': 'code_login'})),
    path('putpwd/',views.PutPwdViewSet.as_view({'post': 'putpwd'})),
]
