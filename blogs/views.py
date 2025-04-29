from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy

from blogs.models import BlogEntry


class BlogsListView(ListView):
    """Отображение главной страницы"""
    model = BlogEntry
    template_name = "blogs/blogs_list.html"

    def get_queryset(self):
        return BlogEntry.objects.filter(is_publication_attribute=True)


class BlogsCategoriesView(ListView):
    """Отображение всех объектов в категории"""
    model = BlogEntry
    template_name = "blogs/blogs_categories.html"

    def get_queryset(self):
        return BlogEntry.objects.filter(
            category__name=self.kwargs['category'],
            is_publication_attribute=True
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_category'] = self.kwargs['category']
        return context


class BlogCreateView(CreateView):
    """Создание статьи"""
    model = BlogEntry
    template_name = "blogs/blogs_form.html"
    fields = ["title", "description", "preview", "category", "is_publication_attribute"]
    success_url = reverse_lazy("blogs:home_page")


class BlogDetailView(DetailView):
    """Подробнее о статье"""
    model = BlogEntry
    template_name = "blogs/blogs_detail.html"

    def get_object(self, queryset=None):
        """Увеличение счетчика просмотров"""
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_category'] = self.object.category.name
        return context


class BlogUpdateView(UpdateView):
    """Редактирование статьи"""
    model = BlogEntry
    template_name = "blogs/blogs_form.html"
    fields = ["title", "description", "preview", "category", "is_publication_attribute"]

    def get_success_url(self):
        return reverse_lazy("blogs:blog_detail", kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    """Класс для удаления статьи"""
    model = BlogEntry
    template_name = "blogs/blogs_confirm_delete.html"
    success_url = reverse_lazy("blogs:home_page")
