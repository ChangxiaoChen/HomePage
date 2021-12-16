
from rest_framework import serializers
from . import models
import re
from rest_framework.exceptions import ValidationError

class ContactModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Contact
        fields = ['you_name','you_email','you_company','leave_word']
        extra_kwargs ={
            'you_name':{'required':True,'write_only':True},
            'you_email':{'required':True,'write_only':True},
            'you_company':{'required':True,'write_only':True},
            'leave_word':{'required':True,'write_only':True}
        }

    def validatad_you_email(self,data):
        if re.match(data,r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'):
            return data
        else:
            raise ValidationError({'detail':'您的邮箱格式不正确'})