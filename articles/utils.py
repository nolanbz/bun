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
 
    title = object["title"]
    what_is = object["what_is"]
    content = object["content"]
    key_things_to_consider = object["key_things_to_consider"]
    features = object["features"]    
    prices_of_similar_products = object["prices_of_similar_products"]
    faq = object["faq"]
    meta_title = object["meta_title"]
    meta_description = object["meta_description"]
    image_url = object["image_url"]
    aritcle_id = object["id"]
    abunda_slug = object["abunda_slug"]
    published = object["published"]
    tags = object["tags"]

    body_html = f"""
        {content}
        <h2>Key things to consider</h2>
        {key_things_to_consider}
        <h2>Key features</h2>
        {features}       
        <h2>Frequently asked questions</h2>
        {faq}
        <h2>Similar products</h2>
        {prices_of_similar_products}
    """

    abunda_data = {
        "article": 
        { 
            "title": title,
            "summary": what_is,
            "body_html": body_html,
            "backend_id": aritcle_id,
            "image_url": image_url,
            "meta_title": meta_title,
            "meta_description": meta_description, 
            "published": published, 
            "abunda_slug": abunda_slug, 
            "tags": tags, 
        }
    } 

    return abunda_data