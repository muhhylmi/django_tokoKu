import datetime
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .models import *
from .utils import cookieCart, cartData, guestOrder
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import FormCustomer
# Create your views here.


def signup(request):
    if request.POST:
        form = FormCustomer(request.POST)
        # print(request.POST['email'])
        if form.is_valid():
            form.save()
            messages.success(request, "Registrasi Berhasil")
            return redirect('signup')
        else:
            messages.error(request, "Terjadi Kesalahan")
            return redirect('signup')
    else:
        form = FormCustomer()
        konteks = {
            'form': form
        }
    return render(request, "registration/signup.html", konteks)


def store(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def view(request, id_barang):
    data = cartData(request)
    cartItems = data['cartItems']

    product = Product.objects.get(id=id_barang)
    context = {'product': product, 'cartItems': cartItems}
    return render(request, 'store/view.html', context)


def cart(request):
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )
    return JsonResponse('Payment submitted..', safe=False)
