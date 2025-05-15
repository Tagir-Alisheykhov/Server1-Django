from django.db import models


class Category(models.Model):
    """
        Модель для категории продуктов.
    """
    name = models.CharField(max_length=100, verbose_name="Название категории")
    description = models.TextField(
        verbose_name="Описание", blank=True, null=True, help_text="Введите описание"
    )

    def __str__(self):
        """
            Строковое отображение объекта.
        """
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    """
        Модель продукта
    """

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
        verbose_name="Активный товар"
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
