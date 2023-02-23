from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404



from .forms import ArticleForm
from .models import Article
# Create your views here.

def article_search_view(request):
    query = request.GET.get('q')
    qs = Article.objects.search(query=query)
    context = {
        "object_list": qs
    }
    return render(request, "articles/search.html", context=context)


def index(request):
    qs = Article.objects.published()
    template_name = "index.html"
    context = {"object_list": qs}
    return render(request, template_name, context)

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
        return redirect(article_object.get_absolute_url())     
    else:
        print('form invalid')
    return render(request, "articles/create.html", context=context)


@login_required
def article_update_view(request, id=None):

    article_obj = Article.objects.get(id=id)
    
    form = ArticleForm(request.POST or None, instance=article_obj)
    context = {
        "form": form,
        "object": article_obj,        
    }
    if form.is_valid():
        form.save()
        context['message'] = 'Data saved.'

    return render(request, "articles/create.html", context=context)


def article_detail_view(request, slug=None):
    article_obj = None
   
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)            
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first()
        except:
            raise Http404
    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)