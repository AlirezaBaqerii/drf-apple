from django.urls import path

from .views import CategoryList, ProductList, ProductDetail

app_name = 'api'

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
]
