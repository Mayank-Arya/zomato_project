from django import forms
from .models import Dish, Order

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'price', 'availability']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'dish_ids']


class UpdateOrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']
