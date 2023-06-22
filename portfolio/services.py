from django.db.models import QuerySet

from portfolio import models


def work_all(visible=True) -> QuerySet[models.Work]:
    return models.Work.objects.filter(visible=visible)


def language_all() -> QuerySet[models.Work]:
    return models.Language.objects.all()


def technology_all() -> QuerySet[models.Work]:
    return models.Technology.objects.all()
