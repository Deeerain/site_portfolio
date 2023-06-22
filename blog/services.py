from django.db.models import QuerySet

from blog import models


def post_all() -> QuerySet[models.Post]:
    return models.Post.objects\
        .all()


def post_get_newest(count: 5) -> QuerySet[models.Post]:
    return post_all().order_by('created')[:count]
