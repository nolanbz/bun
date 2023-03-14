from rest_framework import serializers

from articles.models import Article
from rest_framework.response import Response
from rest_framework.views import APIView

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = [
            "id",
            "title",            
            "meta_title",
            "meta_description",
            "tags",
            "image_url",
            "summary",
            "abunda_scorecard",
            "content",            
        ]

