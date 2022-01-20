from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, verbose_name="Никнейм")
    email = models.EmailField(max_length=100, verbose_name="Email", unique=True, blank=True)
    profile_image = models.ImageField(upload_to = 'users_profile/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ('-created', )