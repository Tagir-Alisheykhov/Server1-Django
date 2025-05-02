from django.db import models


class Category(models.Model):
    """Класс категорий блоговых-записей (статей)"""
    name = models.CharField(max_length=100, verbose_name="Название категории")
    description = models.TextField(
        verbose_name="Описание", blank=True, null=True, help_text="Введите описание"
    )

    def __str__(self):
        """Строковое представление"""
        return self.name

    class Meta:
        """Метаданные"""
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class BlogEntry(models.Model):
    """Класс модели блоговых-записей"""
    title = models.CharField(
        max_length=70,
        verbose_name="Заголовок",
        help_text="Введите заголовок"
    )
    description = models.TextField(
        verbose_name="Содержимое блога",
        help_text="Введите содержимое блога",
        null=True,
        blank=True
    )
    preview = models.ImageField(
        upload_to="blogs/photo/",
        verbose_name="Изображение",
        help_text="Загрузите изображение",
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания"
    )
    is_publication_attribute = models.BooleanField(
        default=False,
        verbose_name="Состояние публикации",
        help_text="Определите состояние публикации"
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Количество просмотров",
        help_text="Введите количество просмотров публикации",
        default=0
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория статьи",
        blank=True,
        null=True,
        related_name="Articles"
    )

    def __str__(self):
        """Строковое отображение объекта"""
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
