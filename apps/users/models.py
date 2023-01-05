from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized.forms import ResizedImageField

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
    )
    age = models.PositiveSmallIntegerField(
        verbose_name="Возраст",
        blank=True, null=True
    )
    profile_image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='profile_images/',
        verbose_name="Фотография профиля",
        blank = True, null = True
    )
    bio = models.TextField(
        verbose_name="Био",
        blank = True, null = True
    )

    
    def __str__(self):
        return self.username 

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"