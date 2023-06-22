from django.db import models
from ckeditor.fields import RichTextField


class Language(models.Model):
    title = models.CharField('Название', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    def __str__(self) -> str:
        return self.title


class Technology(models.Model):
    title = models.CharField('Название', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Технология'
        verbose_name_plural = 'Технологии'

    def __str__(self) -> str:
        return self.title


class Work(models.Model):
    title = models.CharField('Название', max_length=100, unique=True,
                             db_index=True)
    content = RichTextField()
    github = models.URLField('Github', null=True, db_index=True, blank=True)
    languages = models.ManyToManyField(Language, verbose_name='Языки')
    technologies = models.ManyToManyField(Technology,
                                          verbose_name='Технологии')
    visible = models.BooleanField('Видимость', default=True, db_index=True)
    slug = models.SlugField()
    created = models.DateTimeField('Дата создания', auto_now_add=True,
                                   db_index=True)
    updated = models.DateTimeField('Дата обновления', auto_now=True,
                                   db_index=True)

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def __str__(self) -> str:
        return self.title
