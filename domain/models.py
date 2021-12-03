from django.db import models

    
#class to create events for a wedding with name, budget, date and guest
class Event(models.Model):
    name = models.CharField(null=False, blank=False, unique=True, max_length=200)
    budget = models.DecimalField(null=False, blank=False, max_digits=9, decimal_places=2)
    event_date = models.DateField(null=False, blank=False)
    guest = models.IntegerField(default=1, null=False, blank=False)
    

    def __str__(self):
        return self.name

# create a service with name and description like religious ceremony o reception
class Service(models.Model):
    name = models.CharField(null=False, blank=False, unique=False, max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.name

#create subservice like venues for the reception. Fields name, description ,service, productos
class SubService(models.Model):
    name = models.CharField(null=False, blank=False, max_length=500)
    description = models.TextField()
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    products = models.ManyToManyField('Product')
    
    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("name", "service", )

#create companies that provides the products. Fields name and description
class Supplier(models.Model):
    name = models.CharField(null=False, blank=False, unique=False, max_length=500)
    description = models.TextField()
    
    def __str__(self):
        return self.name

#products or services that providers have to plan the wedding.Fields  
class Product(models.Model):
    name = models.CharField(null=False, blank=False, max_length=500)
    price = models.TextField()
    unit = models.TextField()
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("name", "supplier", )

#create reservation with event, service, subservice, product, quantity, dates
class Reservation(models.Model):    
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    subservice = models.ForeignKey('SubService', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    
    quantity = models.IntegerField(default=1, null=False, blank=False)
    reservation_date = models.DateField(default="2021-11-25", null=False, blank=False)
    start_date = models.DateField(default="2021-11-25", null=False, blank=False)
    finish_date = models.DateField(default="2021-11-25", null=False, blank=False)
    

    def __str__(self):
        return self.event.name


    class Meta:
        unique_together = ("event", "service", "subservice", "product")
