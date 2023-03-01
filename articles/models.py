from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.utils import timezone
# Create your models here.

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

    title = models.TextField()
    meta_title = models.TextField()
    meta_description = models.TextField()
    what_is = models.TextField()
    key_things_to_consider = models.TextField()
    faq = models.TextField()
    features = models.TextField()
    prices_of_similar_products = models.TextField()    
    content = models.TextField()
    image_url = models.URLField(default='https://robohash.org/test.png')
    abunda_slug = models.TextField(blank=True)
    abunda_url = models.URLField(default='https://www.shopabunda.com/blog/')
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255)    
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
    published = models.BooleanField(default=False)
    tags = models.TextField(blank=True)
  
    objects=ArticleManager()

    @property
    def name(self):
        return self.title

    def get_absolute_url(self):
        # return f'/articles/{self.slug}/'
        return reverse("articles:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):    
        super().save(*args, **kwargs)   


def update_abunda_slug(data):
    article_id = data['backend_id']
    abunda_slug = data['slug']
    object = Article.objects.filter(id=article_id).first()
    if object:               
        object.abunda_slug = abunda_slug
        object.abunda_url = f'https://www.shopabunda.com/blog/{abunda_slug}'
        object.save()
        return object     

def article_pre_save(sender, instance, *args, **kwargs):    
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(article_pre_save, sender=Article)


def article_post_save(sender, instance, created, *args, **kwargs):    
    if created:
        slugify_instance_title(instance, save=True)

post_save.connect(article_post_save, sender=Article)