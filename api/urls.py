from django.urls import path
from . import views
from .views import HomeView, AddProductView, UpdateProductView, DeleteProductView

urlpatterns = [
    #path('', views.apiOverview, name='apiOverview'),

    
    path('product-list/',views.ShowAll, name='product-list'),
    path('product-detail/<int:pk>/',views.ViewProduct, name='product-detail'),
    path('product-create/',views.CreateProduct, name='product-create'),
    path('product-update/<int:pk>/',views.UpdateProduct, name='product-update'),
    path('product-delete/<int:pk>/',views.DeleteProduct, name='product-delete'),

    #path('', views.home, name="home"),

    path('product-show/',views.ShowApi, name='product-show'),

    path('', HomeView.as_view(), name="home"),
    path('create_product', AddProductView.as_view(), name='create_product'),
    path('update_product/<int:pk>', UpdateProductView.as_view(), name='update_product'),
    path('delete_product/<int:pk>', DeleteProductView.as_view(), name='delete_product'),
]