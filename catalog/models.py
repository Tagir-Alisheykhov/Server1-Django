from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from transliterate import translit

from users.models import User


class Category(models.Model):
    """
        Модель для категории продуктов.
    """
    name = models.CharField(
        max_length=100,
        verbose_name="Название категории"
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,  # Уникальный slug для каждой категории
        blank=True,
        verbose_name="URL-идентификатор (slug)"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text="Введите описание"
    )

    def __str__(self):
        """
            Строковое отображение объекта.
        """
        return self.name

    def get_unique_slug(self):
        """
            Генерирует уникальный slug на основе названия категории
            с правильной проверкой уникальности
        """
        name_str = str(self.name)
        slug = slugify(name_str)
        if not slug:
            try:
                slug = slugify(translit(name_str, 'ru', reversed=True))
            except:
                slug = 'category'
        if not slug:
            slug = 'category'
        unique_slug = slug
        num = 1
        queryset = Category.objects.all()
        if self.pk:
            queryset = queryset.exclude(pk=self.pk)  # Исключение текущего объекта из проверки.
        while queryset.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


@receiver(pre_save, sender=Category)
def category_pre_save(sender, instance, **kwargs):
    """
    Автоматически заполняет slug перед сохранением объекта.
    """
    if not instance.slug or instance.slug == '':
        instance.slug = instance.get_unique_slug()


class Product(models.Model):
    """
        Модель продукта
    """

    PUBLISH_STATUS = [
        ('published', 'Опубликован'),
        ('unpublished', 'Не опубликован'),
    ]

    publish_status = models.CharField(
        max_length=20,
        choices=PUBLISH_STATUS,
        default='moderation',
        verbose_name='Статус публикации'
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Название товара",
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to="catalog/photo/",
        verbose_name="Изображение",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        blank=True,
        null=True,
        related_name="Products",
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счётчик просмотров",
        help_text="Укажите количество просмотров",
        default=0
    )
    price = models.IntegerField(
        verbose_name="Цена"
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_date = models.DateField(
        auto_now=True,
        verbose_name="Дата обновления"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Готовность товара к продаже"
    )
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец товара",
        help_text="Укажите владельца товара",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        """
            Строковое отображение объекта
        """
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price", "category"]
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
        ]
