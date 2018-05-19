from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ProxySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)

    def get_name(self, obj):
        return obj.author.user.username
    class Meta:
        model = Proxy
        fields = ('name', 'ip', 'created_at', 'is_active')
        lookup_field = 'uuid'


class HostConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostConfig
        fields = ('name', 'ip', 'port', 'status', 'author')
        lookuo_field = 'uuid'