from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    """Заполнение базы данных дефолтными значениями"""
    help = "Add catalog to the database"

    def handle(self, *args, **options):
        # Очищаем базу
        Category.objects.all().delete()
        Product.objects.all().delete()
        # Загружаем данные из фикстуры (JSON-файла)
        call_command("loaddata", "catalog_fixture.json")
        # Выводим успешное сообщение
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
