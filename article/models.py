from django.db import models

# Create your models here.
from user.models import UserInfo

from utils.model import BaseModel


class Article(BaseModel):
    type_choices = ((0, '审核不通过'), (1, '审核已通过'), (3, '未审核'))
    title = models.CharField(max_length=127, null=True, blank=True, verbose_name='文章标题')
    intro = models.CharField(max_length=300, null=True, blank=True, verbose_name='文章简介')
    cover = models.ImageField(upload_to='cover/', default='cover/default.jpg', verbose_name='文章封面')
    content = models.TextField(null=True, blank=True, verbose_name='文章内容')
    author = models.ForeignKey(to=UserInfo, on_delete=models.SET_NULL, null=True, blank=True, db_constraint=False,
                               verbose_name='文章作者')
    check_person = models.SmallIntegerField(choices=type_choices, verbose_name='文章审核状态')

    class Meta:
        db_table = 'homepage_article'
        verbose_name = '文章表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '文章标题：%s，文章作者：%s'%(str(self.title),str(self.author.nickname))
