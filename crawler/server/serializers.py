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
        fields = ('uuid', 'name', 'ip', 'updated_at', 'is_active')
        lookup_field = 'uuid'


class HostConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostConfig
        fields = ('name', 'ip', 'port', 'status', 'author', 'uuid', 'username', 'password')
        lookuo_field = 'uuid'

class JobListSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField(read_only=True)

    def get_status(self, obj):
        return obj.status/999

    class Meta:
        model = Job
        fields = ('uuid', 'tag', 'start_at', 'end_at', 'excute_time', 'author', 'status')
        lookuo_field = 'uuid'

class JobDetailSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField(read_only=True)
    result = serializers.SerializerMethodField(read_only=True)
    last_time = serializers.SerializerMethodField(read_only=True)

    def get_status(self, obj):
        return obj.status/999
    
    def get_result(self, obj):
        try:
            return obj.result.name + ' ' + obj.result.ip + ':' + obj.result.port
        except:
            return ''
    def get_last_time(self, obj):
        return str(obj.start_at)[:10] + '--' + str(obj.end_at)[:10]

    class Meta:
        model = Job
        exclude = ['id']

class DBconfigSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField(read_only=True)

    def get_created_at(self, obj):
        return str(obj.created_at)[:10]

    class Meta:
        model = DBconfig
        fields = '__all__'