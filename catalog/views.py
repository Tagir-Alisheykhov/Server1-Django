from django.http import HttpResponseForbidden
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render

from catalog.forms import ProductForm
from catalog.models import Product


def home(request):
    return render(request, "home.html")


class ContactsView(TemplateView):
    """Страница контактов"""
    template_name = "catalog/contacts.html"
    success_url = reverse_lazy("catalog:products_list")


class ProductListView(ListView):
    """Полный список продуктов"""
    model = Product


class ProductDetailView(DetailView):
    """Детальная информация о продукте"""
    model = Product

    def get_object(self, queryset=None):
        """Увеличение счетчика просмотров"""
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Для создания новых продуктов"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        """
            Автоматическое добавление создателя товара.
        """
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Для обновления карточки товара"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def get(self, request, *args, **kwargs):
        """Проверка права на редактирование карточки товара"""
        self.object = self.get_object()
        is_moderator = request.user.groups.filter(name='ProductModerators').exists()
        if request.user == self.object.owner:
            return super().get(request, *args, **kwargs)
        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("403  -  У вас нет прав на редактирование карточки товара.")
        else:
            return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Проверка прав на изменение статуса publish_status"""
        self.object = self.get_object()
        is_moderator = request.user.groups.filter(name='ProductModerators').exists()
        is_owner = request.user == self.object.owner
        is_superuser = request.user.is_superuser
        if is_moderator or is_owner or is_superuser == True:
            return super().post(request, *args, **kwargs)
        else:
            print(request.user.is_superuser)
            if 'publish_status' in request.POST:
                if request.POST['publish_status'] != str(self.object.publish_status):
                    return HttpResponseForbidden("403  -  У вас нет прав на изменение статуса публикации товара")

    def get_form_kwargs(self):
        """
        Передача пользователя в форму
        для валидации прав на отмену
        публикации.
        """
        kwargs = super().get_form_kwargs()
        # Передача пользователя в форму
        kwargs['user'] = self.request.user
        return kwargs


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление продукта"""
    model = Product
    success_url = reverse_lazy('catalog:products_list')

    def post(self, request, *args, **kwargs):
        """Проверка у пользователя права на удаление товара."""
        self.object = self.get_object()
        is_owner = request.user == self.object.owner
        is_superuser = request.user.is_superuser
        is_moderator = request.user.groups.filter(name='ProductModerators').exists()
        if is_owner or is_moderator or is_superuser is True:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseForbidden('403  -  У вас нет прав на удаление товара')
