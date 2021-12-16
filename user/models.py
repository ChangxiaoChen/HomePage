from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from utils.model import BaseModel


class UserInfo(AbstractUser,BaseModel):
    gender_type = ((0,"男"),(1,"女"),(2,"其他"))
    username= models.CharField(max_length=64,unique=True,null=True)
    mobile = models.CharField(max_length=11,verbose_name='手机号')
    icon = models.ImageField(upload_to='icon/', default='icon/default.jpg',verbose_name='头像')
    is_lock = models.BooleanField(default=False,verbose_name='是否锁定')
    nickname = models.CharField(max_length=128,null=True,blank=True,verbose_name='昵称')
    intro = models.CharField(max_length=256,null=True,blank=True,verbose_name='个性签名')
    gender = models.IntegerField(choices=gender_type,default=0,verbose_name='性别')

    class Meta:
        db_table = 'homepage_userinfo'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.nickname)
