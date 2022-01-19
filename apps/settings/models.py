from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=150)
    logo = models.ImageField(blank=True,upload_to='images/')
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    address = models.CharField(blank=True,max_length=100)
    phone = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=50)
    facebook = models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    telegram = models.CharField(blank=True, max_length=50)
    about_page = RichTextUploadingField(blank=True)
    contact_page = RichTextUploadingField(blank=True)

    def __str__(self):
        return f"ID: {self.id} ||||| Title: {self.title}"
    
    class Meta:
        verbose_name_plural = "Настройки"