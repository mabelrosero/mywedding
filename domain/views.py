from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from domain.models import Product, Service, SubService

def index(request):
    return render(request,  'index.html',  {'name': 'Patricia', 'lastname': 'Rosero'})

@login_required
def services_list(request):
    services = Service.objects.all()
    return JsonResponse({'data': [{'id': s.id, 'name': s.name} for s in services]})


@login_required
def sub_services_list(request, service_id):
    sub_services = SubService.objects.filter(service_id=service_id)
    return JsonResponse({'data': [{'id': s.id, 'name': s.name} for s in sub_services]})

@login_required
def products_by_sub_services_list(request, sub_service_id):
    subservice = SubService.objects.filter(id=sub_service_id)
    if subservice.exists():
        products = subservice.first().products.all()
        return JsonResponse({'data': [{'id': s.id, 'name': s.name} for s in products]})

