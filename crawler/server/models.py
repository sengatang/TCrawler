from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token
import uuid


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        token, created =  Token.objects.get_or_create(user=instance)

# Create your models here.
class TcrawlerUser(models.Model):
    user = models.ForeignKey(User, default=None) 
    institution = models.ForeignKey('Institution', null=True, on_delete=models.SET_NULL, related_name='user_institution', default=None)
    is_admin = models.IntegerField(default=0)

class Institution(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    config = models.ForeignKey('DBconfig', null=True, on_delete=models.SET_NULL, related_name='institution_dbconfig')
    
class Proxy(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('TcrawlerUser', null=True, on_delete=models.SET_NULL, related_name='proxy_user')
    Institution_author = models.ForeignKey('Institution', null=True, on_delete=models.SET_NULL, related_name='proxt_insititution')
    ip = models.CharField(max_length=255, blank=True)
    port = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.IntegerField(default=1)

class DBconfig(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('TcrawlerUser', null=True, on_delete=models.SET_NULL, related_name='dbconfig_user')
    Institution_id = models.ForeignKey('Institution', null=True, on_delete=models.SET_NULL, related_name='dbconfig_institution')
    ip = models.CharField(max_length=255, blank=True)
    port = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    status = models.IntegerField(default=0)  #0 down | 1 running  | 2 fail

class HostConfig(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('TcrawlerUser', null=True, on_delete=models.SET_NULL, related_name='hostconfig_user')
    name = models.CharField(max_length=255, blank=True)
    ip = models.CharField(max_length=255, blank=True)
    port = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    status = models.IntegerField(default=0)  #0 down | 1 success  | 2 fail

class Application(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('TcrawlerUser', null=True, on_delete=models.SET_NULL, related_name='application_user')
    Institution = models.ForeignKey('Institution', null=True, on_delete=models.SET_NULL, related_name='application_institution')
    dbconfig = models.ForeignKey('DBconfig', null=True, on_delete=models.SET_NULL, related_name='application_dbconfig')
    job =  models.ForeignKey('Job', null=True, on_delete=models.SET_NULL, related_name='application_job')
    is_proved = models.IntegerField(default=0) # 1 stands for proved

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField()
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    excute_time = models.TextField()
    author = models.ForeignKey('TcrawlerUser', null=True, on_delete=models.SET_NULL, related_name='job_user')
    institution = models.ForeignKey('Institution', null=True, on_delete=models.SET_NULL, related_name='job_isntitution')
    target_url = models.CharField(max_length=255)
    result = models.ForeignKey('DBconfig', null=True, on_delete=models.SET_NULL, related_name='job_dbconfig')
    status = models.IntegerField(default=0)  #0 down | 1 success  | 2 stopped

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField()
    job = models.ForeignKey('Job', null=True, on_delete=models.SET_NULL, related_name='task_job')
    excute_time = models.TimeField(auto_now_add=True)

