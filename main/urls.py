from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('json/', views.show_products_json, name='show_products_json'),
    path('xml/', views.show_products_xml, name='show_products_xml'),
    path('json/<str:id>/', views.show_product_json_by_id, name='show_product_json_by_id'),
    path('xml/<str:id>/', views.show_product_xml_by_id, name='show_product_xml_by_id'),
    path('add/', views.add_product, name='add_product'),
    path('products/<str:pk>/', views.product_detail, name='product_detail'),
]