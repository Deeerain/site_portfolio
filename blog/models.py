from django.contrib.auth import get_user_model
from django.db import models

from ckeditor.fields import RichTextField


USER_MODEL = get_user_model()


class Post(models.Model):
    title = models.CharField('Название', max_length=100, unique=True,
                             db_index=True)
    content = RichTextField()
    created = models.DateTimeField('Дата создания', auto_now_add=True,
                                   db_index=True)
    updated = models.DateTimeField('Дата обновления', auto_now=True,
                                   db_index=True)
    visible = models.BooleanField('Видимость', default=False, db_index=True)
    thumbnail = models.ImageField('Превью')

    class Meta:
        verbose_name = 'Пост'
        verbose_name = 'Посты'

    def __str__(self) -> str:
        return self.title
