from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import stripe

from basket.basket import Basket
# Create your views here.
@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.','')

    stripe.api_key= 'pk_test_51IM7baB3tBwIFB39MhtaXJH6FlIdeXh68EOq75eWrlwOp0JGa9PTOTQFh58qfQU4NTSSWK69JlfCTHFEFwaSthwY00GDAq0DyQ'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid':request.user.id}
    )

    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})
