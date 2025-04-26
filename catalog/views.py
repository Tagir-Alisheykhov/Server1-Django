from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Product


def home(request):
    return render(request, "home.html")


# def contacts(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         message = request.POST.get("message")
#         return HttpResponse(f"Спасибо {name}! Сообщение получено.")
#     return render(request, "contacts.html")

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
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    """Для создания новых продуктов"""
    model = Product
    fields = ("name", "category", "image", "description", "price")
    success_url = reverse_lazy("catalog:products_list")


class ProductUpdateView(UpdateView):
    """Для обновления карточки товара"""
    model = Product
    fields = ("name", "category", "image", "description", "price")
    success_url = reverse_lazy("catalog:products_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:products_list")