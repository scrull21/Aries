from tabnanny import verbose
from django.db import models
from apps.categories.models import Category

# Create your models here.
class Tags(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ('-created', )

class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_post')
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title, self.category

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ('-created', )

class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'news_images/')