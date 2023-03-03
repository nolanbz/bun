from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ArticleSerializer
from articles.models import Article
from rest_framework.permissions import IsAuthenticated
from articles.utils import build_blog_from_data
from api.utils import post_to_abunda_blog, put_to_abunda_blog
from articles.models import update_abunda_slug
from django.http import JsonResponse


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Article.objects.all().order_by('title')
    serializer_class = ArticleSerializer

    def create(self, request, *args, **kwargs):
        print('hit create')
        # Call the parent class's create() method to perform the default create operation
        response = super().create(request, *args, **kwargs)

        data = build_blog_from_data(response.data)
        print("built data")                

        if data['article']['abunda_slug']:      
           abunda_response = put_to_abunda_blog(data)
           print("put to abunda") 
           
        else:            
            abunda_response = post_to_abunda_blog(data)            
            print("post to abunda") 

            if abunda_response:
                update_abunda_slug(abunda_response)
                print("updated slug") 

        return response
