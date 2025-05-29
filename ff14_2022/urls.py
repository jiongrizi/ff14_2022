"""ff14_2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
# from django.contrib import admin

from server.views import *

urlpatterns = [
    #    url(r'^admin/', admin.site.urls),
    url(r'^ff_key_search$', ff_key_search),
    url(r'^580$', ff_580),
    url(r'^590$', ff_590),
    url(r'^index\.html$', index),
    url(r'^$', index),
]
