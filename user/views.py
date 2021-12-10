from django.shortcuts import render

# Create your views here.

from utils.APIResponse import APIResponse
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from .models import UserInfo
from rest_framework.exceptions import APIException
import re
from utils import get_code
from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings
from .serializers import RegisterSerializer
from .serializers import LoginSerilizers
from .serializers import PutPwdSerilizers
from .serializers import CodeLoginSerilizers
from utils.HomePage_logging import get_logger


logger = get_logger()


def send_emails(type_code,message,email):
    """
    send_emails：
        发送邮件
    tupe_cocde:
        settings.CACHE_LOGIN_SMS
        settings.CACHE_REG_SMS
        settings.CACHE_PUTPWD_SMS
    message:
        message

    email:
        email
    return:
        1 or 0
    """

    verification_code = get_code.get_code()
    cache.set(type_code % email, verification_code, 120)
    return send_mail(message, verification_code,settings.EMAIL_HOST_USER, [email,], fail_silently=False)


class EmailViewSet(ViewSet):

    """
    GET:
        get_email：邮箱是否存在
    GET:
        re_codes：注册获取邮箱验证
    GET:
        login_codes：登录获取邮箱验证码
    GET:
        pwd_codes：修改密码获取邮箱验证
    """

    @action(methods='GET',detail=False)
    def get_email(self,request,*args,**kwargs):
        email = request.query_params.get('email')
        if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
            raise APIException({"detail": "The email number is invalid"})
        try:
            UserInfo.objects.get(email=email)
            raise APIException({"detail":"邮箱号存在"})
        except:
            raise APIException({"detail":"The mailbox number does not exist"})



    @action(methods='GET',detail=False)
    def reg_codes(self,request,*args,**kwargs):
        email=request.query_params.get('email')
        if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
            raise APIException({"detail": "The email number is invalid"})
        res = send_emails(settings.CACHE_REG_SMS, "注册验证码", email)
        if res == 1:
            return APIResponse(code=200,result=[])
        else:
            raise APIException({"detail": "注册邮件发送失败"})

    @action(methods='GET',detail=False)
    def login_codes(self,request,*args,**kwargs):
        email = request.data.get('email')
        if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
            raise APIException({"detail": "The email number is invalid"})
        res = send_emails(settings.CACHE_LOGIN_SMS, "登录验证码", email)
        if res == 1:
            return APIResponse(code=200,result=[])
        else:
            raise APIException({"detail": "登录邮件发送失败"})

    @action(methods='GET',detail=False)
    def pwd_codes(self,request,*args,**kwargs):
        email = request.query_params.get('email')
        if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
            raise APIException({"detail": "The email number is invalid"})
        res = send_emails(settings.CACHE_PUTPWD_SMS, "修改密码验证码", email)
        if res == 1:
            return APIResponse(code=200,result=[])
        else:
            raise APIException({"detail": "修改密码邮件发送失败"})



class RegisterViewSet(ViewSet):
    @action(methods='POST',detail=False)
    def reg(self,request,*args,**kwargs):
        ser = RegisterSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return APIResponse(data=ser.data,result=[])


class LoginViewSet(ViewSet):

    def login(self,request,*args,**kwargs):

        ser = LoginSerilizers(data=request.data,context={'request':request})
        if ser.is_valid(raise_exception=True):
            logger.warning("IP为%s 的 用户:%s 登录了"%(ser.context.get('ip'),ser.context.get('email')))
            result = [{'id':ser.context.get('id'),'token':ser.context.get('token'),'email':ser.context.get('email'),'icon':ser.context.get('icon'),'ip':ser.context.get('ip')}]
            return APIResponse(code=200,result=result)

    def code_login(self,request,*args,**kwargs):
        ser = CodeLoginSerilizers(data=request.data,context={'request':request})
        if ser.is_valid(raise_exception=True):
            logger.warning("IP为%s 的 用户:%s 登录了"%(ser.context.get('ip'),ser.context.get('email')))
            result = [{'id':ser.context.get('id'),'token':ser.context.get('token'),'email':ser.context.get('email'),'icon':ser.context.get('icon'),'ip':ser.context.get('ip')}]
            return APIResponse(code=200,result=result)



class PutPwdViewSet(ViewSet):

    def putpwd(self,request,*args,**kwargs):
        ser = PutPwdSerilizers(data=request.data)
        if ser.is_valid(raise_exception=True):
            return APIResponse(code=200,result=[])














