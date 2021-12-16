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
from utils.getnickname import get_nickname

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
        error_messages={"blank": "请输入密码", "required": "请输入密码", "max_length": "密码不能包含中文，长度6位数以上，并且包含英语与数字", "min_length": "密码不能包含中文，长度6位数以上，并且包含英语与数字"},
        write_only=True, )
    re_password = serializers.CharField(
        required=True,
        min_length=8,
        max_length=16,
        error_messages={"blank": "请输入密码", "required": "请输入密码", "max_length": "密码不能包含中文，长度6位数以上，并且包含英语与数字",
                        "min_length": "密码不能包含中文，长度6位数以上，并且包含英语与数字"},
        write_only=True, )

    class Meta:
        model = UserInfo
        fields = ['code', 'email', 'password','re_password']

    def validate(self, attrs):

        email = str(attrs.get("email"))
        if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
            raise ValidationError({"detail": "邮箱格式错误，请重新输入"})
        code = cache.get(settings.CACHE_REG_SMS % email)
        verification_code = str(attrs.get('code'))
        if verification_code != code:
            raise ValidationError({"detail": "请输入正确的验证码"})
        password = str(attrs.get("password"))
        re_password = str(attrs.get("re_password"))

        if not re.match(r'^[a-zA-Z0-9]{6,18}$', password) and not re.match(r'^[a-zA-Z0-9]{6,18}$', re_password):
            raise ValidationError({"detail": "密码不能包含中文，长度6位数以上，并且包含英语与数字"})
        if password != re_password:
            raise ValidationError({"detail": "密码不一致，请重新输入"})
        return attrs

    def create(self, validated_data):
        validated_data.pop('code')
        validated_data.pop('re_password')
        validated_data['username'] = 'WMS' + validated_data['email']
        validated_data['nickname'] = get_nickname()
        validated_data['intro'] = '我的签名'
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
        self.context['intro'] = user.intro
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

class PasswordPutModelSerializer(serializers.ModelSerializer):
    '''
    修改密码
    '''
    password = serializers.CharField(max_length=18,min_length=6,write_only=True)
    class Meta:
        model = UserInfo
        fields = ['email','password']
        extra_kwargs = {
            'password':{'read_only':False}

        }


    def validate(self, attrs):
        password=attrs.get('password')
        if not re.match(r'^[a-zA-Z0-9]{6,18}$', password) and not re.match(r'^[a-zA-Z0-9]{6,18}$', password):
            raise ValidationError({"detail": "密码不能包含中文，长度6位数以上，并且包含英语与数字"})
        return attrs

    def update(self, instance, validated_data):
        user=UserInfo(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return instance



class UserDetailModelSerializer(serializers.ModelSerializer):
    '''
    用户详情
    '''
    # icon = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
    # suffix = serializers.CharField(allow_blank=False)
    class Meta:
        model = UserInfo
        fields = ['nickname','intro','icon']