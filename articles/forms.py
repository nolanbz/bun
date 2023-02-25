from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'meta_title',
            'meta_description',
            'what_is',
            'key_things_to_consider',
            'faq',
            'features',
            'prices_of_similar_products',                        
        ]
