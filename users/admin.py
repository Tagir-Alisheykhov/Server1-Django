from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
        Создание объекта с пользователями
    """
    list_display = ('id', 'email')
