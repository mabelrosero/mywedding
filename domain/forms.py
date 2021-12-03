from django import forms

from .models import Product, Reservation, Service, SubService

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        #fields = "__all__"
        exclude = ['subservice_id']

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        
        # self.base_fields['service'].queryset.filter(id=1)

        try:
            self.initial['service'] = kwargs['instance'].service.id
        except:
            pass
        service_list = [('', '---------')] + [(i.id, i.name) for i in Service.objects.all()]

        try:
            self.initial['subservice'] = kwargs['instance'].subservice.id
            subservice_list = [(i.id, i.name) for i in SubService.objects.filter(
                service_id=kwargs['instance'].service.id
            )]
        except:
            subservice_list = [('', '---------')]

        try:
            self.initial['product'] = kwargs['instance'].product.id

            subservice = SubService.objects.filter(service_id=kwargs['instance'].service.id)
            if subservice.exists():
                product_list = [(i.id, i.name) for i in subservice.first().products.all()]
        except:
            product_list = [('', '---------')]


        # Override the form, add onchange attribute to call the ajax function
        self.fields['service'].widget = forms.Select(
            attrs={
                'id': 'id_service',
                'onchange': 'getSubService(this.value)',
                'style': 'width:200px'
            },
            choices=service_list,
        )
        
        self.fields['subservice'].widget = forms.Select(
            attrs={
                #'id': 'id_subervice',
                'onchange': 'getProduct(this.value)',
                'style': 'width:200px'
            },
            choices=subservice_list
        )

        self.fields['product'].widget = forms.Select(
             choices=product_list
        )        

        print(kwargs)