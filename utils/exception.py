from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.views import Response
from rest_framework import status
from utils import HomePage_logging
logger = HomePage_logging.get_logger()



def exception_handler(exc, context):
    # 记录日志
    try:
        user_id = context['request'].user.id
    except:
        user_id = '该用户未登录'
    logger.critical('视图类：%s 出错了，是IP地址为 %s 的用户访问，用户id为： %s ，错误原因是 %s' % (
    str(context['view']), context['request'].META.get('REMOTE_ADDR'), user_id, str(exc)))
    print('视图类：%s 出错了，是IP地址为 %s 的用户访问，用户id为： %s ，错误原因是 %s' % (
    str(context['view']), context['request'].META.get('REMOTE_ADDR'), user_id, str(exc)))

    response = drf_exception_handler(exc, context)
    if response is None:
        # 记录服务器异常
        logger.critical('%s' % exc)
        response = Response({'detail': '服务器异常，请重试...'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return response
