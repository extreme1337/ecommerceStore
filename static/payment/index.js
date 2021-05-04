var stripe = Stripe('pk_test_51IM7baB3tBwIFB39MhtaXJH6FlIdeXh68EOq75eWrlwOp0JGa9PTOTQFh58qfQU4NTSSWK69JlfCTHFEFwaSthwY00GDAq0DyQ')

var elem = document.getElementById('submit');
clientsecret = elem.getAttribute('data-secret');

var elements = stripe.elemenst()
var style = {
    base: {
        color: "#000",
        lineHeight: '2.4',
        fontSize: '16px'
    }
};

var card = elements.create("card", {'style': style});
card.mount("#card-element");

card.on('change', function(event){
    var displayError = document.getElementById('card-errors')
    if(event.error){
        displayError.textContent = event.error.message;
        $('#card-errors').addClass('alert alert-info');
    }else{
        displayError.textContent = '';
        $('#card-errors').removeClass('alert alert-info');
    }
});

var form = document.getElementById('payment-form');
form.addEventListener('submit', function(ev){
    ev.preventDefault();

    var custName = document.getElementById('custName').nodeValue;
    var custAdd = document.getElementById('custAdd').nodeValue;
    var custAdd2 = document.getElementById('custAdd2').nodeValue;
    var postCode = document.getElementById('postCode').nodeValue;


    stripe.ConfirmCardPayment(clientsecret, {
        payment_method:{
            card: card,
            billing_details:{
                address:{
                    line1: custAdd,
                    line2: custAdd2
                },
                name: custName
            },
        }
    }).then(function(result){
        if(result.error){
            console.log('payment error')
            console.log(result.error.message);
        }else{
            if(result.paymentIntent.status === 'succeeded'){
                console.log('payment processed')

                window.location.replace("http://127.0.0.1:8000/payment/orderplaced/");
            }
        }
    })
});