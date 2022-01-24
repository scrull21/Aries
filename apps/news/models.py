from tabnanny import verbose
from django.db import models
from apps.categories.models import Category
from apps.users.models import User

# Create your models here.
class Tags(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ('-created', )

class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_post')
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.category}"

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ('-created', )

class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name = 'post_image')
    image = models.ImageField(upload_to = 'news_images/')

class NewsLike(models.Model):
    news_liked = models.ForeignKey(News, on_delete=models.CASCADE, related_name="news_liked")
    liked_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_user")

    def __str__(self):
        return self.news_liked

    class Meta:
        verbose_name = "Лайк новостя"
        verbose_name_plural = "Лайкл новостей"
        ordering = ('-news_liked', )

class NewsComment(models.Model):
    news_comment = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_comment')
    comment_title = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_title 

    class Meta:
        verbose_name = "Комент новостя"
        verbose_name_plural = "Коменты новостей"
        ordering = ('-created', )