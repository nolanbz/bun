from rest_framework import serializers

from articles.models import Article
from rest_framework.response import Response
from rest_framework.views import APIView

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = [
            "title",
            "content",
            "meta_title",
            "meta_description",
            "what_is",
            "key_things_to_consider",
            "faq",
            "features",
            "prices_of_similar_products",                        
            "id",
            "published",
            "tags",
            "abunda_slug",
            "image_url",
        ]

