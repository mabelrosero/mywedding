from typing import Any, Optional
from django.contrib import admin
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelChoiceField
from django.http.request import HttpRequest

from domain.forms import ReservationForm
from .models import Event, Product, Reservation, Service, SubService, Supplier


#an event
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "budget", "event_date", "guest", "get_total")

    def get_total(self, obj):
        reservations = Reservation.objects.filter(event_id=obj.id)
        reservations = list(reservations)
        total = 0
        for r in reservations:
            total += float(r.product.price)
        return total

#a service DCT
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "description", )
    
#add subservice to service 
@admin.register(SubService)
class SubServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "service", )
   
#providers of products 
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "description", )
    
#products of the suppliers  
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "unit", "supplier",)
    

# @admin.register(SubServiceForEvent)
# class SubServiceForEventAdmin(admin.ModelAdmin):
#     list_display = ("name", "subservice", "event", )
#     #search_fields = ("name__startswith", )    

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    form = ReservationForm

    class Media:
        js = (
            'js/chained-area.js',
        )
    list_display = ("event", "service", "subservice", "product", "quantity", "product", "get_price" )
    #search_fields = ("name__startswith", )   
 
    def get_price(self, obj):
        return obj.product.price
