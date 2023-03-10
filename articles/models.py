from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.utils import timezone


from .utils import slugify_instance_title

User = settings.AUTH_USER_MODEL

class ArticleQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups) 

class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)

class Article(models.Model):

    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    title = models.TextField(blank=True)
    meta_title = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    tags = models.TextField(blank=True)
    image_url = models.URLField(default='https://robohash.org/test.png')
    summary = models.TextField(blank=True)
    content = models.TextField(blank=True)

    abunda_slug = models.TextField(blank=True)
    abunda_url = models.URLField(default='https://www.shopabunda.com/blog/')
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255)    
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
    published = models.BooleanField(default=False)

    # Old stuff need to remove
    what_is = models.TextField(blank=True)
    key_things_to_consider = models.TextField(blank=True)
    faq = models.TextField(blank=True)
    features = models.TextField(blank=True)
    prices_of_similar_products = models.TextField(blank=True)    
  
    objects=ArticleManager()

    @property
    def name(self):
        return self.title

    def get_absolute_url(self):        
        return reverse("articles:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):    
        super().save(*args, **kwargs)   
        

def article_pre_save(sender, instance, *args, **kwargs):    
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(article_pre_save, sender=Article)


def article_post_save(sender, instance, created, *args, **kwargs):    
    if created:
        slugify_instance_title(instance, save=True)

post_save.connect(article_post_save, sender=Article)