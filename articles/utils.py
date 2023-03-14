import random
from django.utils.text import slugify

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

def build_blog_from_data(instance):

    aritcle_id = instance.id
    title = instance.title
    meta_title = instance.meta_title
    meta_description = instance.meta_description
    tags = instance.tags
    image_url = instance.image_url
    summary = instance.summary
    abunda_scorecard = instance.abunda_scorecard
    content = instance.content

    abunda_slug = instance.abunda_slug
    published = instance.published


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
            "abunda_scorecard": abunda_scorecard,
            "body_html": content,
            "abunda_slug": abunda_slug,
            "published": published,     
        }
    } 

    return abunda_data