from django.shortcuts import render

# Create your views here.
from utils.APIResponse import APIResponse

from . import models
from rest_framework.viewsets import ModelViewSet
from .serializers import ArticleModelSerializer
from utils.check_jwt_authenticate import MyJSONWebTokenAuthentication
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from utils.page import MyPageNumberPagination
class ArticleView(ModelViewSet):
    """
        retrieve:
            作者查询一篇文章

        list:
            作者查询所有文章

        create:
            新增一篇文章

        delete:
            删除一篇文章

        partial_update:
            修改一篇文章

        update:
            修改一篇文章
    """

    queryset = models.Article.objects.filter().all()
    serializer_class = ArticleModelSerializer
    authentication_classes = [MyJSONWebTokenAuthentication]
    pagination_class = MyPageNumberPagination
    def get_object(self):
        return self.request.user


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_delete=True
        instance.save()
        self.get_serializer(instance=instance,many=False)
        return APIResponse(msg={'msg':'删除文章成功'})



class BrowseArticleView(GenericViewSet,RetrieveModelMixin,ListModelMixin):
    """
    list:
        未登录可以查看 所有文章
    retrieve：
        未登录可以查看 单篇文章

    """
    queryset = models.Article.objects.all()
    serializer_class = ArticleModelSerializer
    # authentication_classes = [MyJSONWebTokenAuthentication]
    pagination_class = MyPageNumberPagination
    def retrieve(self, request, *args, **kwargs):
        serializer = super().retrieve(request, *args, **kwargs)
        result = [serializer.data]
        return APIResponse(code=200,result=result)
    def list(self, request, *args, **kwargs):
        serializer = super().list(request, *args, **kwargs)
        result = [serializer.data]
        return APIResponse(code=200,result=result)













