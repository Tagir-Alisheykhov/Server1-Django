from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """
        Модель для создания пользователя.
    """

    email = models.EmailField(
        unique=True,
        verbose_name="Email"
    )
    phone_number = PhoneNumberField(
        blank=True,
        null=True,
        verbose_name="Телефон"
    )
    country = CountryField(
        blank=True,
        null=True
    )
    avatar = models.ImageField(
        upload_to="avatars/",
        blank=True,
        null=True
    )
    # Токен необходим для верификации пользователя по почте.
    token = models.CharField(
        max_length=100,
        verbose_name="Token",
        blank=True,
        null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
