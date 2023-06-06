from django.shortcuts import render, redirect, HttpResponse
import stripe
from payments.models import Product

stripe.api_key = "sk_test_51MzuoMEVPKSh1ZLpzslhIQDhuz7a8eDrWt9AYAMoczpX9d1SFb6sfVnXJHzBKcxpgQI4p7rew8oFOwNm01qXvSIe00AUmMV9PG"

def home(request):
    products = Product.objects.all()
    return render(request, 'checkout.html',{"products":products})

def checkout(request, pid):
    obj = Product.objects.get(id=pid)
    print("Product name: ",obj.name)
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': obj.api,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url="http://127.0.0.1:8000" + '/success',
            cancel_url="http://127.0.0.1:8000" + '/cancel',
        )
    except Exception as e:
        return str(e)
    return redirect(checkout_session.url, code=303)

def success(request):
    return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')