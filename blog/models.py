# -*- coding=utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

# 用户模型.
#第一种：采用的继承方式扩展用户信息（本系统采用）
#扩展：关联的方式去扩展用户信息
class User(AbstractBaseUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200, blank=True, null=True, verbose_name='用户头像')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username

class Tag(models.Model):
	name = models.CharField(max_length='30',verbose_name='标签名称')

	 class Mete:
		 verbose_name = '标签'
         verbose_name_plual = verbose_name

     def __unicode__(self):
		 return  self.name


class Catagory(models.Model):
	name = models.CharField(max_length='30', verbose_name='分类名称')
	index = models.CharField(default=999,verbose_name='分类的排序')

	 class Mete:
		 verbose_name = '分类'
         verbose_name_plual = verbose_name

     def __unicode__(self):
		 return  self.name