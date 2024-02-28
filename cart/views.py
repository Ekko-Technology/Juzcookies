from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Order, OrderedItems
from .forms import CheckoutForm
import json
from decimal import Decimal

# Create your views here.
def items(request):
    # obtain data from user's account cart
    if request.method == "GET":
        if request.user.is_authenticated:
            orders = Order.objects.all()
            return render(request, 'cart.html', {'orders': orders})
        # if user is guest data from session's cart
        else:
            orders = request.session.get('cart', {})
            return render(request, 'cart.html', {'orders': orders})
    
    elif request.method == 'POST':
        # update Order database quantity in session-based cart
        # un-jsonify the data back into a Dict
        data = json.loads(request.body)
        item_id = data["item_id"]
        quantity = data["quantity"]
        # update session-cartbased on AJAX data
        if quantity == 0:
            del request.session["cart"][item_id]
            print(request.session['cart'])
        else:
            request.session['cart'][item_id]['quantity'] = quantity
            print(request.session['cart'])
        
        request.session.save()  # Save the session after making changes
    
        return JsonResponse({'status': 'success'})

        # # Calculate the new total price and total quantity of the cart
        # total_quantity = 0
        # total_price = 0
        # for item in request.session['cart'].values():
        #     total_quantity += item['quantity']
        #     total_price += item['price'] * item['quantity']
        # # Return updated cart data as JSON response
        # return JsonResponse({'total_quantity': total_quantity, 'total_price': total_price})

    
def checkout(request):

    if request.user.is_authenticated:
        orders = Order.objects.all()
    # if user is guest data from session's cart
    else:
        orders = request.session.get('cart', {})
        
    
    if request.method == 'POST':
        # obtain default form created in forms.py
        form = CheckoutForm(request.POST)
        if form.is_valid():
             # access session-based cart
            cart = request.session.get('cart', {})
            item_dict = dict()
            total_price_cart = Decimal(0)
            # iterate through items 
            for product_id, item in cart.items():
                quantity = item['quantity']
                price = Decimal(item['price'])
                # calculate and update total price
                item_price = quantity * price
                total_price_cart += item_price
                # insert new key-value pair
                item_dict[item['name']] = quantity
            
             # Convert item_dict to a JSON string
            item_dict_json = json.dumps(item_dict)

            ordered_item = OrderedItems(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                telephone_number=form.cleaned_data['telephone_number'],
                address=form.cleaned_data['address'],
                unit_number=form.cleaned_data['unit_number'],items_ordered = item_dict_json,
                total_price = total_price_cart
            )
            ordered_item.save()

            # clear cart and redirect back to homepage
            request.session['cart'] = {}
            return redirect('home') 


    else:
        form = CheckoutForm()
    
    return render(request, 'checkout.html', {'form': form, 'orders': orders})
            