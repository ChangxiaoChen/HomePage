from django.db import models

# Create your models here.
from utils.model import BaseModel


class Contact(BaseModel):
    you_name = models.CharField(max_length=64,null=True,blank=True,verbose_name='您的名字')
    you_email = models.EmailField(null=True,blank=True,verbose_name='您的邮箱')
    you_company = models.CharField(max_length=127,null=True,blank=True,verbose_name='您的企业名字')
    leave_word = models.CharField(max_length=300,null=True,blank=True,verbose_name='留言')

    class Meta:
        db_table='homepage_contact'
        verbose_name='联系我们表'
        verbose_name_plural=verbose_name

    def __str__(self):
        return "名字：%s 邮箱：%s 企业%s 给我们联系"%(str(self.you_name),str(self.you_email),str(self.you_company))



