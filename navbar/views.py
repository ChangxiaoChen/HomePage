import json

from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet
from .models import Navbar
from .serializers import NavbarModelSerializer
from utils.APIResponse import APIResponse

class NavbarView(GenericViewSet,ListAPIView):
    '''
    list:

    '''

    queryset = Navbar.objects.filter().all()
    serializer_class = NavbarModelSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return APIResponse(code=200,result=serializer.data)



