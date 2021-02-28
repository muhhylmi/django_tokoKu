import json
from .models import *


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    items = []
    order = {'get_cart_items': 0, 'get_cart_total': 0}
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]['quantity']

            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            order['get_cart_items'] += cart[i]['quantity']
            order['get_cart_total'] += total

            item = {
                'product': {
                    'id': product.id,
                    'price': product.price,
                    'name': product.name,
                    'imageURL': product.imageURL
                },
                'quantity': cart[i]['quantity'],
                'get_total': total
            }
            items.append(item)
        except:
            pass
    return {'items': items, 'order': order, 'cartItems': cartItems}


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        # Create empty cart for now for non-logged in user
        cookieData = cookieCart(request)
        items = cookieData['items']
        order = cookieData['order']
        cartItems = cookieData['cartItems']
    return{'items': items, 'order': order, 'cartItems': cartItems}
