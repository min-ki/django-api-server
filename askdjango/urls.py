"""askdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('sample/', include('sample.urls', namespace='sample')),
    path('ep03/', include('ep03.urls', namespace='ep03')),
    path('ep04/', include('ep04.urls', namespace='ep04')),
    path('ep06/', include('ep06.urls', namespace='ep06')),
    path('ep08/', include('ep08.urls', namespace='ep08')),
]
