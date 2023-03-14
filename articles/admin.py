from django.contrib import admin

# Register your models here.
from .models import Article
from articles.utils import build_blog_from_data
from api.utils import post_to_abunda_blog, put_to_abunda_blog

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'timestamp', 'updated']
    search_fields = ['title', 'content']
    raw_id_fields = ['user']

    # def save_model(self, request, obj, form, change):
    #     print('hit save')
    #     super().save_model(request, obj, form, change)


        # data = {
        #     'id': obj.id,
        #     'title': obj.title,
        #     'meta_title': obj.meta_title,
        #     'meta_description': obj.meta_description,
        #     'tags': obj.tags,
        #     'image_url': obj.image_url,
        #     'summary': obj.summary,
        #     'abunda_scorecard': obj.abunda_scorecard,
        #     'content': obj.content,
            
        #     'abunda_url': obj.abunda_url,            
        #     'abunda_slug': obj.abunda_slug,            
        #     'published': obj.published,
            
        # }

        # data = build_blog_from_data(data)
        # print(data)
        # print("built data")
        
        # if obj.abunda_slug:
        #    response = put_to_abunda_blog(data)
        #    print(response)
        # else:
        #     response = post_to_abunda_blog(data)
        #     print(response)
        #     print("posted to abunda") 

admin.site.register(Article, ArticleAdmin)