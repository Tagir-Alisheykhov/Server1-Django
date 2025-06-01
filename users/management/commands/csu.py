from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
        Класс для создания суперпользователя.
        Для создания пользователя с помощью данного класса
        необходимо ввести в терминале команду `python manage.py [('filename')=('csu')]`
    """

    def handle(self, *args, **kwargs):
        """
            Параметры суперпользователя.
        """
        user = User.objects.create(email="admin@example.com")
        user.set_password("12345")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.id = 1
        user.save()
