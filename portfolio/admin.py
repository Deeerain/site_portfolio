from django.contrib import admin
from portfolio import models


@admin.register(models.Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated', 'visible')
    list_editable = ('visible',)
    list_filter = ('created', 'updated', 'visible')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('title',)
