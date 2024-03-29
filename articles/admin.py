from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from api.utils import send_to_abunda_blog

from .models import Article

class PublishedListFilter(admin.SimpleListFilter):
    title = _('Published')
    parameter_name = 'published'

    def lookups(self, request, model_admin):
        return (
            ('published', _('Published')),
            ('unpublished', _('Unpublished')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'published':
            return queryset.filter(published=True)
        elif self.value() == 'unpublished':
            return queryset.filter(published=False)
        return queryset
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'timestamp', 'updated']
    search_fields = ['title', 'content']
    raw_id_fields = ['user']
    list_filter = (PublishedListFilter,)

    def delete_model(self, request, obj):
        send_to_abunda_blog(obj.abunda_slug, 'DELETE')
        print("deleted")       
        super().delete_model(request, obj)


admin.site.register(Article, ArticleAdmin)