"""geekshop URL Configuration

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
from django.views.generic.base import RedirectView
from mainapp import views as mainapp_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    path('', RedirectView.as_view(url="/index", permanent=False)),
    path('index/', mainapp_views.main, name = "index"),
    path('products/', include('mainapp.urls', namespace ='products'), name = 'products'),
    path('contact/', mainapp_views.contact, name = "contact"),
    path('basket/', include('basketapp.urls', namespace='basket')),
    # админка из коробки (defaultadmin) и пользовательская (adminapp)
    #path('defaultadmin/', admin.site.urls),
    path('admin/', include('adminapp.urls', namespace='admin')),
    path('auth/', include('authapp.urls', namespace='auth'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)