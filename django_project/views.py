import os
import random
import math
import requests
import environ
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.shortcuts import render, redirect

@require_http_methods(['GET', 
'POST'])
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
    libraries = [0,2,2]
    return render(request, 'index.html', {
        'libraries': libraries,
        'public_key': 'FLWPUBK_TEST-d1765bbd42307aad3ccb6fa9d59e21d9-X',
    })



vars = ['DoesNotExist', 
'MultipleObjectsReturned', 
'STATUS_CANCELED', 
'STATUS_CHOICE', 
'STATUS_EXPIRED', 
'STATUS_PAID', 
'STATUS_PENDING', 
'STATUS_REFUNDED', 
'_Order__initial_status_paid_or_pending', 
'all_fees', 
'all_logentries', 
'all_logentries_link', 
'all_positions', 
'annotate_overpayments', 
'assign_code', 
'banktransaction_set', 
'cachedcombinedticket_set', 
'can_modify_answers', 
'cancel_allowed', 
'cancellation_date', 
'cancellation_requests', 
'check', 
'checkin_attention', 
'clean', 
'clean_fields', 
'code', 
'comment', 
'count_positions', 
'create_transactions', 
'custom_followup_at', 
'custom_followup_due', 
'customer', 
'customer_id', 
'date_error_message', 
'datetime', 
'delete', 
'download_reminder_sent', 
'email', 
'email_confirm_hash', 
'email_known_to_work', 
'event', 
'event_id', 
'expires', 
'expiry_reminder_sent', 
'fees', 
'from_db', 
'full_clean', 
'full_code', 
'get_deferred_fields', 
'get_next_by_datetime', 
'get_next_by_expires', 
'get_next_by_last_modified', 
'get_previous_by_datetime', 
'get_previous_by_expires', 
'get_previous_by_last_modified', 
'get_status_display', 
'gift_card_transactions', 
'gracefully_delete', 
'id', 
'invoice_address', 
'invoices', 
'is_expired_by_time', 
'last_modified', 
'locale', 
'log_action', 
'logs_content_type', 
'meta_info', 
'meta_info_data', 
'net_total', 
'normalize_code', 
'objects', 
'payment_refund_sum', 
'payment_term_last', 
'payments', 
'pending_sum', 
'phone', 
'pk', 
'positions', 
'positions_with_tickets', 
'prepare_database_save', 
'propose_auto_refunds', 
'referencedpaypalobject_set', 
'referencedstripeobject_set', 
'refresh_for_update', 
'refresh_from_db', 
'refunds', 
'require_approval', 
'resend_link', 
'sales_channel', 
'save', 
'save_base', 
'secret', 
'send_mail', 
'serializable_value', 
'set_expires', 
'status', 
'tax_total', 
'testmode', 
'ticket_download_available', 
'ticket_download_date', 
'top_logentries', 
'top_logentries_has_more', 
'total', 
'touch', 
'transactions', 
'unique_error_message', 
'user_cancel_allowed', 
'user_cancel_deadline', 
'user_cancel_fee', 
'user_change_allowed', 
'user_change_deadline', 
'validate_unique']

vars2 = [
'amount', 
'confirm', 
'create_external_refund', 
'created', 
'fail', 
'fee', 
'gift_card_transactions', 

'info', 
'info_data', 

'local_id', 
'objects', 
'order_id', 

'payment_date', 
'payment_provider', 
'provider', 
'refunded_amount', 
'refunds', 
]