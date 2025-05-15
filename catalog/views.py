from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
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


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Для обновления карточки товара"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:products_list")
