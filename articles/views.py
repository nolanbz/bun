from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render



from .forms import ArticleForm
from .models import Article

@login_required(login_url='/login/')
def index(request):
    qs = Article.objects.published()
    template_name = "index.html"
    context = {"object_list": qs}
    return render(request, template_name, context)

@login_required(login_url='/login/')
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