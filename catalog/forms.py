from django.forms import ModelForm
from django.core.exceptions import ValidationError

from catalog.models import Product

FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар"
]


class ProductForm(ModelForm):
    """
        Настройка формы для создания, обновления товаров.
    """
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ("views_counter", "owner")

    def __init__(self, *args, **kwargs):
        """
            Стилизация формы и проверки:
        """
        # Получение пользователя из kwargs
        self.user = kwargs.pop('user', None)
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "SSD-250gb"
        })
        self.fields["description"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Супер скорость.."
        })
        self.fields["image"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Вставьте изображение"
        })
        self.fields["category"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Выберите категорию"
        })
        self.fields["price"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите цену на продукт"
        })
        # Стилизация булевого поля (например, is_active)
        if "is_active" in self.fields:
            self.fields["is_active"].widget.attrs.update({
                "class": "form-check-input",  # Bootstrap класс для чекбокса
            })
            # Для правильного отображения чекбокса в Bootstrap можно добавить обертку
            self.fields["is_active"].label = "Активный товар"  # Подпись поля

    def clean_name(self):
        """
            Валидация поля с названием товара.
        """
        name = self.cleaned_data.get("name")
        for keyword in FORBIDDEN_WORDS:
            if name.strip() == keyword.upper() or name.strip() == keyword.lower():
                raise ValidationError(
                    f"Слово '{name}' входит в список запрещенных слов!"
                )
        return name

    def clean_description(self):
        """
            Валидация поля с описанием товара.
        """
        description = self.cleaned_data.get("description")
        for keyword in FORBIDDEN_WORDS:
            if keyword.upper() in description or keyword.lower() in description:
                raise ValidationError(
                    f"Слово '{description}' входит в список запрещенных слов!"
                )
        return description

    def clean_price(self):
        """
            Валидация на корректный ввод цены.
        """
        price = self.cleaned_data.get("price")
        if int(price) < 0:
            raise ValidationError(
                f"Цена на товар не должна быть отрицательным числом!"
            )
        return price

