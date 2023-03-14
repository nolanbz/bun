from rest_framework import viewsets
from .serializers import ArticleSerializer
from articles.models import Article
from rest_framework.permissions import IsAuthenticated

class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Article.objects.all().order_by('title')
    serializer_class = ArticleSerializer
