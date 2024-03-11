from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# # Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=20)
#     mobile = models.CharField(max_length=11, unique=True)

class User(AbstractUser):
    mobile = models.CharField(max_length=20)

    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户管理'
        verbose_name_plural = '用户管理'