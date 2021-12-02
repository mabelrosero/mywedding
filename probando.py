import django
django.setup()
from domain.models import Product, Service, SubService

# for ser in Service.objects.all():
#     print(ser.__dict__)

# for suser in SubService.objects.all():
#     print(suser.__dict__)

for suser in SubService.objects.all():
    print(type(suser))
    for p in  suser.products.all():
        print(suser.name, p.name)


sub1 = SubService.objects.filter(id=1)
print(sub1.count())
if sub1.exists():
    print("************",sub1.first().name)
    for p in  sub1.first().products.all():
        print(sub1.first().name, p.name)
