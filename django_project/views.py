import os
import random
import math
import requests
import environ
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.shortcuts import render, redirect

@require_http_methods(['GET', 'POST'])
def payment_response(request):
    status=request.GET.get('status', None)
    tx_ref=request.GET.get('tx_ref', None)
    print(status)
    print(tx_ref)
    return render(request, 'flutterwave/payment_callback.html', {
        'payment_status': status,
        'tx_ref': tx_ref,
    })


def process_payment(name,email,amount,phone):
    auth_token= 'FLWSECK_TEST-a987ec54fe7b47dfa301709a3a4096d5-X'
    hed = {'Authorization': 'Bearer ' + auth_token}
    data = {
        "tx_ref":'' + str(math.floor(1000000 + random.random()*9000000)),
        "amount":amount,
        "currency":"ZMW",
        "redirect_url": "http://localhost:8000/callback",
        "payment_options":"card, mobilemoneyghana, barter",
        "meta":{
            "consumer_id":23,
            "consumer_mac":"92a3-912ba-1192a"
        },
        "customer":{
            "email":email,
            "phonenumber":phone,
            "name":name
        },
        "customizations":{
            "title": "Membership Payment",
            "description": "chase your dreams with the right tool -> Books",
            "logo":"https://photo.designxel.com/static/vector/2015/3/14/facegfx-vector-creative-book-combinatorial-library-logo-vector.jpg"
        }
    }
    url = ' https://api.flutterwave.com/v3/payments'
    response = requests.post(
        url, 
        json=data, 
        headers=hed,
    )
    response=response.json()
    link=response['data']['link']
    return link
    

@require_http_methods(['GET', 'POST'])
def index(request):
    name=  'Patrick Patrick'
    email = 'patrick@gmail.com'
    amount = 150
    phone = '260762412680'
    if request.method=='POST':
        return redirect(
            str(
                process_payment(
                    name=name,
                    email=email,
                    amount=amount,
                    phone=phone
                )
            )
        )
    libraries = [0,2,2]
    return render(request, 'index.html', {
        'libraries': libraries,
        'customer': dict(
            name = name,
            email = email,
            amount = amount,
            phone = phone,    
        ),
        'public_key': 'FLWPUBK_TEST-d1765bbd42307aad3ccb6fa9d59e21d9-X',
    })

