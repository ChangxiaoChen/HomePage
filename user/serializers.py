from rest_framework import serializers
from django.core.cache import cache
from django.conf import settings
from rest_framework.exceptions import ValidationError
import re
from .models import UserInfo
from utils.HomePage_logging import get_logger

from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler
from utils import get_code
from django.core.mail import send_mail

logger = get_logger()

class RegisterSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(required=True,write_only=True)
    code = serializers.CharField(
        required=True,
        min_length=6,
        max_length=6,
        write_only=True,
        error_messages={"blank": "请输入验证码", "required": "请输入验证码", "max_length": "验证码格式错误", "min_length": "验证码格式错误"},
        help_text="验证码")
    password = serializers.CharField(
        required=True,
        min_length=8,
        max_length=16,
        error_messages={"blank": "请输入密码", "required": "请输入密码", "max_length": "密码最长16个字符", "min_length": "密码最短8个字符"},
        write_only=True, )

    class Meta:
        model = UserInfo
        fields = ['code', 'email', 'password']

    def validate(self, attrs):
        verification_code = str(attrs.get('code'))
        email = str(attrs.get("email"))
        if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
            raise ValidationError({"detail": "邮箱格式不正确"})
        code = cache.get(settings.CACHE_REG_SMS % email)

        if verification_code != code:
            raise ValidationError({"detail": "验证码错误"})

        return attrs

    def create(self, validated_data):
        validated_data.pop('code')
        validated_data['username'] = 'WMS' + validated_data['email']
        res = UserInfo.objects.create_user(**validated_data)
        res.save()
        print(validated_data.get('email') + '注册成功')
        return res


class LoginSerilizers(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'email', 'password', 'icon']
        extra_kwargs = {
            'id': {
                'read_only': True,
            },
            'icon': {
                'read_only': True,
            },
            "email": {"write_only": True, 'required': True},
            "password": {"write_only": True, "max_length": 16, "min_length": 8, 'required': True}
        }

    def validate(self, attrs):
        user = self._get_user(attrs)
        token = self._get_token(user)
        request = self.context.get('request')
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            self.context['ip'] = request.META.get("HTTP_X_FORWARDED_FOR")
        else:
            self.context['ip'] = request.META.get("REMOTE_ADDR")
        request = self.context['request']
        icon = 'http://%s%s%s' % (request.META['HTTP_HOST'], settings.MEDIA_URL, user.icon)
        self.context['icon'] = icon
        self.context['token'] = token
        self.context['email'] = user.email
        self.context['id'] = user.id
        return attrs

    # 获取用户
    def _get_user(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        print(password)
        if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
            raise ValidationError({"detail": "邮箱格式不正确"})
        user_obj = UserInfo.objects.filter(email=email).first()
        if user_obj is None:
            raise ValidationError({"detail": "用户名或密码错误"})
        EERROR_PWD = {}
        if not user_obj.check_password(password):

            if email not in EERROR_PWD:
                EERROR_PWD[email] = 1
            else:
                EERROR_PWD[email] += 1
            if EERROR_PWD[email] == 3:
                verification_code = get_code.get_code()
                cache.set(settings.CACHE_LOGIN_SMS % email, verification_code, 120)  # 将验证码存入缓存中，过期时间为2分钟
                print(verification_code)
                res = send_mail(
                    "登录验证码",
                    verification_code,
                    settings.EMAIL_HOST_USER,
                    [email, ], fail_silently=False)
                EERROR_PWD[email] = 0
            raise ValidationError({"detail": "用户名或密码错误"})
        return user_obj

    def _get_token(self, user):
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token


class PutPwdSerilizers(serializers.ModelSerializer):
    code = serializers.CharField(
        required=True,
        min_length=6,
        max_length=6,
        write_only=True,
        error_messages={"blank": "请输入验证码", "required": "请输入验证码", "max_length": "验证码格式错误", "min_length": "验证码格式错误"},
        help_text="验证码")

    re_password = serializers.CharField(
        required=True,
        min_length=8,
        max_length=16,
        error_messages={"blank": "请输入密码", "required": "请输入密码", "max_length": "密码最长16个字符", "min_length": "密码最短8个字符"},
        write_only=True, )
    password = serializers.CharField(
        required=True,
        min_length=8,
        max_length=16,
        error_messages={"blank": "请输入密码", "required": "请输入密码", "max_length": "密码最长16个字符", "min_length": "密码最短8个字符"},
        write_only=True, )

    class Meta:
        model = UserInfo
        fields = ['code', 'email', 'password', 're_password']

    def validate(self, attrs):
        email = str(attrs.get("email"))
        if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
            raise ValidationError({"detail": "邮箱格式不正确"})
        verification_code = str(attrs.get('code'))
        code = cache.get(settings.CACHE_PUTPWD_SMS % email)
        if verification_code != code:
            raise ValidationError({"detail": "验证码错误"})
        attrs.pop('code')
        password = attrs.get('password')
        re_password = attrs.get('re_password')
        if password != re_password:
            raise ValidationError({"detail": "密码不一致"})
        attrs.pop('re_password')
        user = UserInfo.objects.filter(email=email).first()
        user.set_password(password)
        user.save()
        return attrs


class CodeLoginSerilizers(serializers.ModelSerializer):
    code = serializers.CharField(
        required=True,
        min_length=6,
        max_length=6,
        write_only=True,
        error_messages={"blank": "请输入验证码", "required": "请输入验证码", "max_length": "验证码格式错误", "min_length": "验证码格式错误"},
        help_text="验证码")

    class Meta:
        model = UserInfo
        fields = ['id','code', 'email']

    def validate(self, attrs):
        user = self._get_user(attrs)
        token = self._get_token(user)
        request = self.context.get('request')
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            self.context['ip'] = request.META.get("HTTP_X_FORWARDED_FOR")
        else:
            self.context['ip'] = request.META.get("REMOTE_ADDR")
        request = self.context['request']
        icon = 'http://%s%s%s' % (request.META['HTTP_HOST'], settings.MEDIA_URL, user.icon)
        self.context['icon'] = icon
        self.context['email'] = user.email
        self.context['id'] = user.id
        self.context['token'] = token
        return attrs

    def _get_user(self, attrs):
        email = str(attrs.get("email"))
        if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
            raise ValidationError({"detail": "邮箱格式不正确"})
        verification_code = str(attrs.get('code'))
        code = cache.get(settings.CACHE_LOGIN_SMS % email)
        if verification_code != code:
            raise ValidationError({"detail": "验证码错误"})
        attrs.pop('code')
        user = UserInfo.objects.filter(email=attrs['email']).first()
        return user

    def _get_token(self, user):
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token


