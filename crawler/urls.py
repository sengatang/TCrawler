"""crawler URL Configuration

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
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers, authtoken
from crawler.server import views
from crawler.server.views import *

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/', authtoken.views.obtain_auth_token, name='user_login'),
    url(r'^logout/', LogoutView.as_view(), name='user_logout'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^register/$', CrawlerUserRegisterView.as_view(), name='user_register'),
    url(r'^proxy/detail/$', ProxyDetailView.as_view(), name='proxy_detail'),
    url(r'^proxy/list/$', ProxyView.as_view(), name='proxy_list'),
    url(r'^host/list/$', HostConfigView.as_view(), name='host_list'),

]