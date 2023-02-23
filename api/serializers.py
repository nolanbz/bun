from rest_framework import serializers

from articles.models import Article

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
            "prices_of_simular_products",
            "simular_products",
            "keywords",
        ]
