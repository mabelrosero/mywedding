from django.urls import path

from . import views

urlpatterns=[
    path('', views.index, name='index' ),
    path('services_list', views.services_list, name='services_list' ),
    path('sub_services_list/<int:service_id>', views.sub_services_list, name='sub_services_list' ),
    path('products_by_sub_services_list/<int:sub_service_id>', views.products_by_sub_services_list, name='products_by_sub_services_list' ),
]