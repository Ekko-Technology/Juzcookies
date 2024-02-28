from django.shortcuts import render, redirect, HttpResponse
from .models import Pastries, Cakes
from django.contrib.auth.decorators import login_required
from cart.models import Order
from decimal import Decimal

# Create your views here.
def pastries(request):
    pastries = Pastries.objects.all()
    if request.method == 'GET':
        return render(request, 'pastries.html', {'pastries':pastries})
    
    # obtain data from form submission
    else:
        try:
            product_id = request.POST.get('pastry-id')
            quantity = int(request.POST.get('quantity', 1))
            pastry = Pastries.objects.get(pk=product_id)

            if request.user.is_authenticated:
                existing_order = Order.objects.filter(pastry=pastry).first()
                if existing_order:
                    existing_order.quantity += quantity
                    existing_order.save()
                else:
                    Order.objects.create(pastry=pastry, quantity=quantity)
            else:
                cart = request.session.get('cart', {})
                cart_item = cart.get('pastry_' + product_id, {'quantity': 0})
                cart_item['name'] = pastry.title
                cart_item['price'] = str(pastry.price)
                cart_item['quantity'] += quantity
                cart_item['image'] = pastry.image.url
                cart['pastry_' + product_id] = cart_item
                request.session['cart'] = cart

            return redirect('pastries')
        except (ValueError, Pastries.DoesNotExist):
            return HttpResponse("Bad data has been inputted. Please resubmit the form.")




def cakes(request):
    cakes = Cakes.objects.all()
    if request.method == 'GET':
        return render(request, 'cakes.html', {'cakes':cakes})
    else:
        try:
            product_id = request.POST.get('cake-id')
            quantity = int(request.POST.get('quantity', 1))
            cake = Cakes.objects.get(pk=product_id)

            # create and save the order object
            if request.user.is_authenticated:
                Order.objects.create(cake=cake, quantity=quantity)
            else:
                # Create or update cart in session
                cart = request.session.get('cart', {})
                cart_item = cart.get('cake_' + product_id, {'quantity': 0})
                cart_item['name'] = cake.title
                cart_item['price'] = str(cake.price)
                cart_item['quantity'] += quantity
                cart_item['image'] = cake.image.url
                cart['cake_' + product_id] = cart_item
                request.session['cart'] = cart

            return redirect('cakes')
        
        except (ValueError, Cakes.DoesNotExist):
            return HttpResponse("Bad data has been inputted. Please resubmit the form.")
        

