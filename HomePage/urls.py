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
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.views import serve
from django.views.static import serve as static_serve
from . import views
def return_static(request, path, insecure=True, **kwargs):
  return serve(request, path, insecure, **kwargs)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="HomePage--API Docs",
        default_version='v1',
        description="这是一个HomePage接口文档",
        terms_of_service="https://www.56yhz.com/",
        # contact=openapi.Contact(email="xxx@qq.com"),
        license=openapi.License(name="Apache License 2.0"),
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),   # 权限类
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='dist/spa/index.html')),
    re_path(r'^favicon\.ico$', views.favicon, name='favicon'),
    re_path('^css/.*$', views.css, name='css'),
    re_path('^js/.*$', views.js, name='js'),
    re_path('^static/.*$', views.statics, name='static'),
    re_path('^fonts/.*$', views.fonts, name='fonts'),
    re_path(r'^static/(?P<path>.*)$', return_static, name='static'),
    re_path(r'^media/(?P<path>.*)$', static_serve, {'document_root': settings.MEDIA_ROOT}),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('user/api/v1/',include('user.urls')),
    path('nav/api/v1/',include('navbar.urls')),
    path('article/api/v1/',include('article.urls')),
    path('contact/api/v1/',include('contactus.urls')),
]
