function getSubService(service_id) {
    let $ = django.jQuery;
    $.get('/domain/sub_services_list/' + service_id, function (resp){
        let sub_service_list = '<option value="" selected="">---------</option>'
        $.each(resp.data, function(i, item){
            sub_service_list += '<option value="'+ item.id +'">'+ item.name +'</option>'
        });
        $('#id_subservice').html(sub_service_list);
    });
}

function getProduct(sub_service_id) {
    let $ = django.jQuery;
    $.get('/domain/products_by_sub_services_list/' + sub_service_id, function (resp){
        let product_list = '<option value="" selected="">---------</option>'
        $.each(resp.data, function(i, item){
            product_list += '<option value="'+ item.id +'">'+ item.name +'</option>'
        });
        $('#id_product').html(product_list);
    });
}

