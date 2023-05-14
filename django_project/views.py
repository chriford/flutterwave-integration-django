import os
import random
import math
import requests
import environ
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Hotel
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response

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
        "redirect_url": "http://localhost:8003/callback",
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
    if request.method=='POST':
        name=  'Siame Chriford'
        email = 'siamechrif@gmail.com'
        amount = request.POST.get('amount')
        float(amount)
        phone = '260762412680'
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
    libraries = Hotel.objects.order_by('name').all()
    return render(request, 'index.html', {
        'libraries': libraries,
        'public_key': 'FLWPUBK_TEST-d1765bbd42307aad3ccb6fa9d59e21d9-X',
    })



class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
        
def hotel_search(request, query):
    if not query:
        return redirect('/')
    hotel_queryset = Hotel.objects.filter(
        name__icontains = query
    )
    hotel_data_seriazer = HotelSerializer(hotel_queryset, many=True)
    return JsonResponse({
        'status': True,
        'payload': hotel_data_seriazer.data,
    })
    
