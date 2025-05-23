from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Клас пользователь"""
    username = models.CharField(
        max_length=50,
        blank=True,
        unique=False
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Почта"
    )
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Телефон"
    )
    city = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name="Город"
    )
    avatar = models.ImageField(
        upload_to="users/avatar",
        blank=True,
        null=True,
        verbose_name="Аватар"
    )
    tg_chat_id = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Telegram chat_id"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username',]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
