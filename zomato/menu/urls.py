from django.urls import path
from . import views

urlpatterns = [
    path('', views.dish_list, name='dish_list'),
    path('add/', views.add_dish, name='add_dish'),
    path('update/<int:dish_id>/', views.update_dish, name='update_dish'),  # URL for updating a dish
    path('delete/<int:dish_id>/', views.delete_dish, name='delete_dish'),
    path('take_order/', views.take_order, name='take_order'),  # URL for taking a new order
    path('update_order_status/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('order_list/', views.order_list, name='order_list'),
    path('order_details/<int:order_id>/', views.order_details, name='order_details'), # URL pattern for dish list
    # Define URLs for adding, updating, and deleting dishes
    # ...
]
