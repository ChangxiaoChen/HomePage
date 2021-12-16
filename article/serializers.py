from rest_framework import serializers
from . import models


class ArticleModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Article
        fields = ['id','title', 'intro', 'cover', 'content', 'author','create_time','updata_time']
