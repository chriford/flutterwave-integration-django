from os import name
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django_project.views import index, payment_response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('callback', payment_response, name='payment_response')
 ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
