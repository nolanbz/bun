from django.contrib import admin

# Register your models here.
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


admin.site.register(Article, ArticleAdmin)