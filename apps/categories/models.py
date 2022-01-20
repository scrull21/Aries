from django.db import models
from apps.users.models import User

# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="category_user")
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to = 'category_image/')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ('-title', )