from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import stripe
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView


from basket.basket import Basket
# Create your views here.
@login_required
def BasketView(request):

    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    stripe.api_key = 'sk_test_51IM7baB3tBwIFB397vqAR3lyATiievboTA95iUrB1g5D1EJqTzIuIxkvxDZOpggSqUAlXNFOxm5u6QlJsY9LLJxR00ghZbeIoF'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )

    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_form(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)
    
    if event.type == 'payment_intent.succeded':
        payment_confirmation(event.data.objects.client_secret)
    else:
        print('Unhandled event type {}'.format(event.type))
    return HttpResponse(status=200)

def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'payment/orderplaced.html')
