from django.urls import path
from blogs.apps import BlogsConfig
from blogs.views import (
    BlogsListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    BlogsCategoriesView
)

app_name = BlogsConfig.name

urlpatterns = [
    path("blogs/list/", BlogsListView.as_view(), name="home_page"),
    path("blogs/detail/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blogs/category/<str:category>/", BlogsCategoriesView.as_view(), name="category_entries"),
    path("blogs/create/", BlogCreateView.as_view(), name="crete_entry"),
    path("blogs/update/<int:pk>/", BlogUpdateView.as_view(), name="update_entry"),
    path("blogs/delete/<int:pk>/", BlogDeleteView.as_view(), name="delete_entry")
]
