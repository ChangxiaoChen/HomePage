from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from rest_framework_jwt.utils import jwt_decode_handler, jwt_get_user_id_from_payload_handler
from user import models
import jwt


class MyCheck_WebTokenAuthentication(BaseAuthentication):

    def authenticate_header(self, request):
        token = request.META.get('HTTP_TOKEN')
        if not (token):
            raise exceptions.AuthenticationFailed({'detail': '未携带token'})
        try:
            payload = jwt_decode_handler(token)
        except jwt.ExpiredSignature:
            msg = {'detail': '签名已经过期'}
            raise exceptions.AuthenticationFailed(msg)
        except jwt.DecodeError:
            msg = {'detail': '错误token签名'}
            raise exceptions.AuthenticationFailed(msg)
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed()
        user_id = jwt_get_user_id_from_payload_handler(payload)
        user = models.UserInfo.objects.filter(pk=user_id).first()
        return (user, token)
