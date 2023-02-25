from django.contrib import admin

# Register your models here.
from .models import Article
from articles.utils import build_blog_from_data
from api.utils import post_to_abunda_blog, put_to_abunda_blog
from articles.models import update_abunda_slug

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'timestamp', 'updated']
    search_fields = ['title', 'content']
    raw_id_fields = ['user']

    def save_model(self, request, obj, form, change):
        print('hit save')
        super().save_model(request, obj, form, change)


        data = {
            'title': obj.title,
            'what_is': obj.what_is,
            'content': obj.content,
            'key_things_to_consider': obj.key_things_to_consider,
            'features': obj.features,
            'prices_of_similar_products': obj.prices_of_similar_products,
            'faq': obj.faq,
            'meta_title': obj.meta_title,
            'meta_description': obj.meta_description,
            'id': obj.id,
            'abunda_slug': obj.abunda_slug,
            'published': obj.published,
            'tags': obj.tags,
        }

        data = build_blog_from_data(data)
        print("built data")
        

        if obj.abunda_slug:
           response = put_to_abunda_blog(data)
           print(response)
        else:
            response = post_to_abunda_blog(data)
            print(response)
            print("posted to abunda") 

            if response:
                update_abunda_slug(response)

admin.site.register(Article, ArticleAdmin)