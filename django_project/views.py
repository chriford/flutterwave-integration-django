import environ
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


def index(request):
    libraries = [0,2,2]
    return render(request, 'index.html', {
        'libraries': libraries,
        'public_key': 'FLWPUBK_TEST-d1765bbd42307aad3ccb6fa9d59e21d9-X',
        'private_key': 'FLWSECK_TEST-a987ec54fe7b47dfa301709a3a4096d5-X',
        'encryption_key': 'FLWSECK_TEST1dc50b94be9c',
    })




@require_http_methods(['GET', 'POST'])
def payment_response(request):
    status=request.GET.get('status', None)
    tx_ref=request.GET.get('tx_ref', None)
    print(status)
    print(tx_ref)
    return HttpResponse('Finished')