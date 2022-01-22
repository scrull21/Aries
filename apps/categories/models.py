from django.db import models
from apps.users.models import User
from django.db.models.signals import pre_save
from utils.slug_generator import unique_slug_generators


# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="category_user")
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to = 'category_image/')
    slug = models.SlugField(blank=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ('-title', )

def slag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generators(instance)


pre_save.connect(slag_pre_save_receiver, sender=Category)