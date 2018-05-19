from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.template import RequestContext, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status, generics, permissions, views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from crawler.server.serializers import UserSerializer, GroupSerializer, ProxySerializer
from .serializers import *

from .models import *
#token
for user in User.objects.all():
    Token.objects.get_or_create(user=user)

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

class CrawlerUserRegisterView(views.APIView):
    authentication_classes = ()
    permission_classes = ()
    def post(self, request):
        # try:
        user = User.objects.create_user(username=request.data['username'], password=request.data['password'], email=request.data['email'])
        user.save()
        api_user = TcrawlerUser()
        api_user.user = user
        institution = request.data['ins']
        if institution is '' or institution is None:
            api_user.institution = None
            api_user.is_admin = 0
        else:
            api_user.institution = Institution.objects.get(id=institution)
            api_user.is_admin = request.data['is_admin']
        api_user.save()
        return Response('success')

class LogoutView(APIView):
    queryset = User.objects.all()
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response("success")

class ProxyDetailView(views.APIView):
    def post(self, request):
        return

class ProxyView(generics.ListCreateAPIView):
    serializer_class = ProxySerializer
    def get_queryset(self):
        try:
            tuser = TcrawlerUser.objects.get(user=self.request.user)
        except:
            return Response("Error")
        return Proxy.objects.filter(author=tuser).order_by('id')
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tuser = TcrawlerUser.objects.get(user=self.request.user)
        instance = serializer.save(
           author=tuser
        )
        response = serializer.data
        headers = self.get_success_headers(response)
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)   

class ProxyDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProxySerializer
    def get_queryset(self):
        try:
            tuser = TcrawlerUser.objects.get(user=self.request.user)
        except:
            return Response("Error")
        return Proxy.objects.filter(author=tuser).order_by('id')

    def post(self, request, *args, **kwargs):
        try:
            ipconfig = Proxy.objects.get(uuid=request.data['formdata[uuid]'])
        except:
            raise Exception
        ipconfig.ip = request.data['formdata[ip]']
        ipconfig.is_active = request.data['formdata[is_active]']
        ipconfig.save()
        return Response('success')

class ProxyDelView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProxySerializer
    queryset = Proxy.objects.filter().order_by('-id')
    lookup_field = 'uuid'

class HostConfigView(generics.ListCreateAPIView):
    serializer_class = HostConfigSerializer
    def get_queryset(self):
        tuser = TcrawlerUser.objects.get(user=self.request.user)
        return HostConfig.objects.filter(author=tuser).order_by('id')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tuser = TcrawlerUser.objects.get(user=self.request.user)
        instance = serializer.save(
           author=tuser
        )
        response = serializer.data
        headers = self.get_success_headers(response)
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)