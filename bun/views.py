
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article




def home_view(request, *args, **kwargs):
   
    # from the database??
    article_obj = Article.objects.all().first()
    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "object": article_obj,
        'user': request.user,        
    }
    # Django Templates
    HTML_STRING = render_to_string("home.html", context=context)
 
    return HttpResponse(HTML_STRING)

