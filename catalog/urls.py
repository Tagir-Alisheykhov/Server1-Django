from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (ProductListView,
                           ProductListByCategoryView,
                           ProductDetailView,
                           ProductCreateView,
                           ProductUpdateView,
                           ProductDeleteView,
                           ContactsView)


app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('category/<slug:category_slug>/', ProductListByCategoryView.as_view(), name='category'),
    path('catalog/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='products_detail'),
    path('catalog/create/', ProductCreateView.as_view(), name='products_create'),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='products_update'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='products_delete'),
    path('catalog/contacts/', ContactsView.as_view(), name='contacts_page'),
]
