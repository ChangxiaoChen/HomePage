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
from utils import HomePage_logging
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from utils.check_jwt_authenticate import MyJSONWebTokenAuthentication
from .serializers import UserDetailModelSerializer
from .serializers import PasswordPutModelSerializer

logger = HomePage_logging.get_logger()


def send_emails(type_code, message, email, sendtype):
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
    email = str(email)
    subject = 'HomePage社区'

    verification_code = get_code.get_code()
    cache.set(type_code % email, verification_code, 120)
    recipient_list = [email, ]
    to = []
    if sendtype == 1:  # 注册验证码
        html_message = "<h1>%s，欢迎您注册HomePage社区 </h1>您的注册验证码是：%s<br/>" % (str(email), verification_code)
        return send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, html_message=html_message)
    elif sendtype == 2:  # 登录验证码
        html_message = "<h1>%s，欢迎您登录HomePage社区 </h1>您的登录验证码是：%s<br/>" % (str(email), verification_code)
        return send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, html_message=html_message)
    elif sendtype == 3:  # 修改密码验证码
        html_message = "<h1>%s，欢迎您登录HomePage社区 </h1>您的修改密码验证码是：%s<br/>" % (str(email), verification_code)
        return send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, html_message=html_message)


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

    @action(methods='GET', detail=False)
    def get_email(self, request, *args, **kwargs):
        email = request.query_params.get('email')
        if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
            raise APIException({"detail": "The email number is invalid"})
        email_obj = UserInfo.objects.filter(email=email).first()
        if email_obj:
            raise APIException({"detail": "用户已存在"})
        else:
            return APIResponse(code=200, msg='邮箱可以注册')

    @action(methods='GET', detail=False)
    def reg_codes(self, request, *args, **kwargs):
        email = request.query_params.get('email')
        if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
            raise APIException({"detail": "The email number is invalid"})

        res = send_emails(settings.CACHE_REG_SMS, "注册验证码", email, 1)
        if res == 1:
            return APIResponse(code=200, result=[])
        else:
            raise APIException({"detail": "注册邮件验证码发送失败，请重新发送"})

    @action(methods='GET', detail=False)
    def login_codes(self, request, *args, **kwargs):
        email = request.data.get('email')
        if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
            raise APIException({"detail": "The email number is invalid"})
        res = send_emails(settings.CACHE_LOGIN_SMS, "登录验证码", email, 2)
        if res == 1:
            return APIResponse(code=200, result=[])
        else:
            raise APIException({"detail": "登录邮件验证码发送失败，请重新发送"})

    @action(methods='GET', detail=False)
    def pwd_codes(self, request, *args, **kwargs):
        email = request.query_params.get('email')
        if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
            raise APIException({"detail": "The email number is invalid"})
        res = send_emails(settings.CACHE_PUTPWD_SMS, "修改密码验证码", email, 3)
        if res == 1:
            return APIResponse(code=200, result=[])
        else:
            raise APIException({"detail": "修改密码邮件验证码发送失败，请重新发送"})


class RegisterViewSet(ViewSet):
    """
    POST:
        reg注册接口
        参数：1、code 2、password 3、re_password

    """

    @action(methods='POST', detail=False)
    def reg(self, request, *args, **kwargs):
        ser = RegisterSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return APIResponse(data=ser.data, result=[])


class LoginViewSet(ViewSet):
    """
    POST:
        login登录接口
        参数：1、email 2、password
    POST:
        code_login 验证码登录
        参数：1、code 2、email
    """

    @action(methods='POST', detail=False)
    def login(self, request, *args, **kwargs):

        ser = LoginSerilizers(data=request.data, context={'request': request})
        if ser.is_valid(raise_exception=True):
            logger.warning("IP为%s 的 用户:%s 登录了" % (ser.context.get('ip'), ser.context.get('email')))
            result = [
                {'id': ser.context.get('id'), 'token': ser.context.get('token'), 'email': ser.context.get('email'),
                 'icon': ser.context.get('icon'), 'ip': ser.context.get('ip')}]
            return APIResponse(code=200, result=result)
        else:
            raise APIException({"detail": "用户名或密码错误"})

    @action(methods='POST', detail=False)
    def code_login(self, request, *args, **kwargs):
        ser = CodeLoginSerilizers(data=request.data, context={'request': request})
        if ser.is_valid(raise_exception=True):
            logger.warning("IP为%s 的 用户:%s 登录了" % (ser.context.get('ip'), ser.context.get('email')))
            result = [
                {'id': ser.context.get('id'), 'token': ser.context.get('token'), 'email': ser.context.get('email'),
                 'icon': ser.context.get('icon'), 'intro': ser.context.get('intro'), 'ip': ser.context.get('ip')}]
            return APIResponse(code=200, result=result)


class PutPwdViewSet(ViewSet):
    """
    put：修改密码

    json数据格式{
    "email": "329025421@qq.com",
    "code": "449921",
    "password": "012345678",
    "re_password": "012345678"
}
    """

    def putpwd(self, request, *args, **kwargs):
        ser = PutPwdSerilizers(data=request.data)
        if ser.is_valid(raise_exception=True):
            return APIResponse(code=200, result=[])


class PasswordPutView(GenericViewSet, UpdateModelMixin):
    """
    put:
        个人中心修改密码

    """

    queryset = UserInfo.objects.filter().all()
    serializer_class = PasswordPutModelSerializer
    authentication_classes = [MyJSONWebTokenAuthentication, ]

    def update(self, request, *args, **kwargs):
        serializer = super().update(request, *args, **kwargs)
        result = [serializer.data]
        return APIResponse(result=result)


class UserDetailView(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    """
    retrieve:
        查看用户自己的信息

    update：
        更新用户自己的信息
    """

    queryset = UserInfo.objects.filter().all()
    serializer_class = UserDetailModelSerializer
    authentication_classes = [MyJSONWebTokenAuthentication, ]

    def get_object(self):
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        serializer = super().retrieve(request, *args, **kwargs)
        result = [serializer.data]
        return APIResponse(result=result)

    def update(self, request, *args, **kwargs):
        serializer = super().update(request, *args, **kwargs)
        result = [serializer.data]
        return APIResponse(result=result)
