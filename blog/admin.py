from django.contrib import admin

from blog import models
from blog.forms import PostAdminForm


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'visible', 'created', 'updated')
    list_editable = ('visible',)
    list_filter = ('created', 'updated', 'visible')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(models.Rubric)
class RubricAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
