from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from rest_framework_jwt.utils import jwt_decode_handler
from user import models
import jwt
from rest_framework.authentication import get_authorization_header


class MyJSONWebTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        jwt_value = get_authorization_header(request)
        if not jwt_value:
            raise exceptions.AuthenticationFailed('未登录，没有Token')
        try:
            payload = jwt_decode_handler(jwt_value)
        except jwt.ExpiredSignature:
            raise exceptions.AuthenticationFailed('签名过期')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('非法用户')
        user = models.UserInfo.objects.filter(pk=payload['user_id']).first()
        return user, jwt_value
