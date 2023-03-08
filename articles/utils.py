import random
from django.utils.text import slugify
import urllib
import requests

def slugify_instance_title(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        # auto generate new slug
        rand_int = random.randint(300_000, 500_000)
        slug = f"{slug}-{rand_int}"
        return slugify_instance_title(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance

def build_blog_from_data(object):

    aritcle_id = object["id"]
    title = object["title"]
    meta_title = object["meta_title"]
    meta_description = object["meta_description"]
    tags = object["tags"]
    image_url = object["image_url"]
    summary = object["summary"]
    content = object["content"]

    abunda_slug = object["abunda_slug"]
    published = object["published"]


    abunda_data = {
        "article": 
        { 
            "backend_id": aritcle_id,
            "title": title,
            "meta_title": meta_title,
            "meta_description": meta_description,
            "tags": tags,
            "image_url": image_url,
            "summary": summary,
            "body_html": content,
            "published": published, 
            "abunda_slug": abunda_slug, 
        }
    } 

    return abunda_data