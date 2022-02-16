from django.db import models
from django.core import validators

class User(models.Model):
    '''用户表'''
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    phone = models.CharField(unique=True,max_length=11,validators=[validators.RegexValidator("1[3456789]\d{9}",message='请输入正确格式的手机号码！')])
    lan_name = models.CharField(max_length=256)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'