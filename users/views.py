import secrets

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User
from config.settings import EMAIL_HOST_USER


class RegisterUserView(CreateView):
    """
        Класс представления для регистрации новых пользователей.
    """

    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """
            Верификация пользователя через почту.
        """
        user = form.save()
        user.is_active = False
        # Генерация токена.
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        # Генерация ссылки для пользователя.
        host = self.request.get_host()  # Получаем хост (откуда пришел пользователь).
        url = f'http://{host}/users/email-confirm/{token}/'
        # Отправка сообщения пользователю.
        send_mail(
            subject='Подтверждение почты',
            message=f'Привет!\nПерейти по ссылке для подтверждения почты {url}',
            from_email=EMAIL_HOST_USER,  # email приложения
            recipient_list=[user.email],  # email пользователя
        )
        return super().form_valid(form)


def email_verification(request, token):
    """
        Endpoint, который будет работать по URL
        и верифицировать пользователя.
        :param request:
        :param token: Для подключения пользователя.
        :return:
    """
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))
