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
