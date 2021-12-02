function getService(service_id) {
    let $ = django.jQuery;
    $.get('/domain/sub_services_list/' + service_id, function (resp){
        let kabupaten_list = '<option value="" selected="">---------</option>'
        $.each(resp.data, function(i, item){
           kabupaten_list += '<option value="'+ item.id +'">'+ item.name +'</option>'
        });
        $('#id_subservice').html(kabupaten_list);
    });
}

