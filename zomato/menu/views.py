from django.shortcuts import render, redirect
from .models import Dish, Order
from .forms import DishForm
from .forms import OrderForm, UpdateOrderStatusForm


# Create your views here.


def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'menu/dish_list.html', {'dishes': dishes})


def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = DishForm()
    return render(request, 'menu/add_dish.html', {'form': form})


def update_dish(request, dish_id):
    dish = Dish.objects.get(dish_id=dish_id)
    form = DishForm(instance=dish)
    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    return render(request, 'menu/update_dish.html', {'form': form})

def delete_dish(request, dish_id):
    dish = Dish.objects.get(dish_id=dish_id)
    if request.method == 'POST':
        dish.delete()
        return redirect('dish_list')
    return render(request, 'menu/delete_dish.html', {'dish': dish})


def take_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.status = 'received'
            order.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'menu/take_order.html', {'form': form})



def update_order_status(request, order_id):
    order = Order.objects.get(order_id=order_id)
    if request.method == 'POST':
        form = UpdateOrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = UpdateOrderStatusForm(instance=order)
    return render(request, 'menu/update_order_status.html', {'form': form})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'menu/order_list.html', {'orders': orders})


def order_details(request, order_id):
    order = Order.objects.get(order_id=order_id)
    return render(request, 'menu/order_details.html', {'order': order})

