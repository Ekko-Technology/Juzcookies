from cart.models import Order

def cart_count(request):
    if request.user.is_authenticated:
        items_count = Order.objects.all().count()
    
    else:
        items_count = 0
        cart = request.session.get('cart', {})
        for count in cart:
            items_count += 1

    return {'cart_count': items_count}
