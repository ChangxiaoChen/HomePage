from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from .models import Contact
from .serializers import ContactModelSerializer
from utils.APIResponse import APIResponse

class ContactView(GenericViewSet,CreateModelMixin):

    queryset = Contact.objects.filter().all()
    serializer_class = ContactModelSerializer

    def create(self, request, *args, **kwargs):
        serializer = super().create(request, *args, **kwargs)
        return APIResponse(code=200,result=serializer.data)

