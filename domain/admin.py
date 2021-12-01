from django.contrib import admin
from .models import Event, Product, Reservation, Service, SubService, SubServiceForEvent, Supplier


#an event
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "budget", "event_date", "guest", )

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
    

@admin.register(SubServiceForEvent)
class SubServiceForEventAdmin(admin.ModelAdmin):
    list_display = ("name", "subservice", "event", )
    #search_fields = ("name__startswith", )    

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity", )
    #search_fields = ("name__startswith", )   
 
