from os import name
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django_project.views import index, payment_response, hotel_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('hotel/query/<str:query>/search/', hotel_search, name="hotel-search"),
    path('callback/', payment_response, name='payment_response')
 ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
