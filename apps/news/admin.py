from django.contrib import admin
from apps.news import models

# Register your models here.
class NewsPostImageAdmin(admin.TabularInline):
    model = models.NewsImage
    extra = 1

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    inlines = [NewsPostImageAdmin]

admin.site.register(models.News, NewsAdmin)
admin.site.register(models.Tags)
admin.site.register(models.NewsLike)
admin.site.register(models.NewsComment)
admin.site.register(models.Advert)