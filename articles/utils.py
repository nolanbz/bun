


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