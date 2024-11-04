from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), blank=True, unique=True)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    profile_picture = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    facebook = models.URLField(max_length=255, blank=True, null=True)
    twitter = models.URLField(max_length=255, blank=True, null=True)
    instagram = models.URLField(max_length=255, blank=True, null=True)
    linkedin = models.URLField(max_length=255, blank=True, null=True)
    tiktok = models.URLField(max_length=255, blank=True, null=True)
    pinterst = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'core_custom_user'
        managed = True
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

