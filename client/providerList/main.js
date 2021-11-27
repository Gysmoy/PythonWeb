function getServices() {
    $.ajax({
        url: ipBack + '/services/getServices/',
        type: 'GET',
        dataType: 'JSON',
        success: res => {
            res.data.forEach(s => {
                var id = s.id;
                var servicio = s.servicio;
                var estado = s.estado;
                $('#servicios').append(`
                <option value="${id}" label="${servicio}" ${!estado ? 'disabled': ''}>${servicio}</option>
                `);
            });
            $.notify('Servicios obtenidos con exito', {
                'position': 'top left',
                'className': 'success'
            });
        },
        error: e => {
            var message = e.responseJSON ? e.responseJSON.message : `Servicios: ${e.statusText}`;
            $.notify(message, {
                'position': 'top left',
                'className': 'error'
            });
        }
    })
}
function getSuppliers() {
    var usuario = getCookie('id');
    $.ajax({
        url: ipBack + '/supplier/getSuppliers/',
        type: 'POST',
        dataType: 'JSON',
        headers: {
            'Content-Type': 'application/json'
        },
        data: JSON.stringify({id: usuario}),
        success: res => {
            var template = '';
            res.data.forEach(proveedor => {
                var data = JSON.stringify(proveedor);
                var tipo = proveedor.tipo == 'N' ? 'PERSONA': 'EMPRESA';
                var nombre;
                if (proveedor.tipo == 'N') {
                    nombre = `${proveedor.apePater} ${proveedor.apeMater}, ${proveedor.nombres}`;
                } else {
                    nombre = proveedor.razonSocial; 
                }
                var documento = proveedor.documento;
                var servicio = proveedor.servicio;
                var tel1 = (proveedor.tel1) ? `Telefono 1: <a href="tel:${proveedor.tel1}">${proveedor.tel1}</a><br>`: '';
                var tel2 = (proveedor.tel2) ? `Telefono 2: <a href="tel:${proveedor.tel2}">${proveedor.tel2}</a><br>`: '';
                var correo = (proveedor.correo) ? `Correo: <a href="mailto:${proveedor.correo}">${proveedor.correo}</a>`: '';
                var contacto = tel1 + tel2 + correo;
                var direccion = proveedor.direccion;
                var estado = proveedor.estado ? 'ACTIVO': 'INACTIVO';
                template += `
                <tr data-proveedor='${data}'>
                    <td>${tipo}</td>
                    <td>${nombre} [${documento}]</td>
                    <td>${servicio}</td>
                    <td>${contacto}</td>
                    <td>${direccion}</td>
                    <td>${estado}</td>
                    <td>
                        <a href="#tbl-providers" id="btn-editar" class="icon solid style1 fa-edit"><span class="label">Editar</span></a>
                        <a href="#tbl-providers" id="btn-estado" class="icon solid style1 fa-toggle-${estado == 'ACTIVO'? 'on': 'off'}"><span class="label">Cambiar estado</span></a>
                    </td>
                </tr>
                `;
            })
            $('#tbl-providers tbody').html(template);
            $('#tbl-providers').DataTable()
            $.notify('Proveedores obtenidos con exito', {
                'position': 'top left',
                'className': 'success'
            });
        },
        error: e => {
            var message = e.responseJSON ? e.responseJSON.message : `Proveedores: ${e.statusText}`;
            $.notify(message, {
                'position': 'top left',
                'className': 'error'
            });
        }
    })
}

$(document).ready(function() {
    getServices();
    getSuppliers();
})

$('#tipoProveedor').change(function() {
    $('#nombres').parent().hide();
    $('#apePater').parent().hide();
    $('#apeMater').parent().hide();
    $('#razonSocial').parent().hide();
    switch ($(this).val()) {
        case 'N':
            $('#nombres').parent().show(250);
            $('#apePater').parent().show(250);
            $('#apeMater').parent().show(250);
            $('#numDoc').attr('placeholder', 'Ingrese N° DNI')    
            break;
        case 'J':
            $('#razonSocial').parent().show(250);
            $('#numDoc').attr('placeholder', 'Ingrese N° RUC')    
            break;
        default:
            $('#numDoc').attr('placeholder', 'Ingrese N° documento')    
            break;
    }
})

$('#addSupplier').click(function() {
    $('#table').hide();
    $('#form').show(250);
    $('#form #title').text('Agregar un proveedor');
    $('#id').val(null);
    $('#tipoConsulta').val('set');
    $('#tipoProveedor').val(null)
        .trigger('change')
        .prop('disabled', false);
    $('#numDoc').val(null);
    $('#apePater').val(null);
    $('#apeMater').val(null);
    $('#nombres').val(null);
    $('#razonSocial').val(null);
    $('#servicios').val(null);
    $('#tel1').val(null);
    $('#tel2').val(null);
    $('#correo').val(null);
    $('#direccion').val(null);
    $('#form form input[type="submit"]').val('AGREGAR');
})
$('#cancelSupplier').click(function() {
    $('#form').hide();
    $('#table').show(250);
})

$(document).on('click', '#btn-editar', function() {
    var row = $(this).parents('tr');
    var data = JSON.parse($(row).attr('data-proveedor'));
    console.log(data)
    $('#form #title').text('Editar un proveedor');
    $('#id').val(data.id_persona);
    $('#tipoConsulta').val('update');
    $('#tipoProveedor').val(data.tipo)
        .trigger('change')
        .prop('disabled', true);
    $('#numDoc').val(data.documento);
    if (data.tipo == 'N') {
        $('#nombres').val(data.nombres);
        $('#apePater').val(data.apePater);
        $('#apeMater').val(data.apeMater);
    } else {
        $('#razonSocial').val(data.razonSocial);
    }
    $('#servicios').val(data.id_servicio);
    $('#tel1').val(data.tel1);
    $('#tel2').val(data.tel2);
    $('#correo').val(data.correo);
    $('#direccion').val(data.direccion);
    $('#form form input[type="submit"]').val('GUARDAR')
    $('#table').hide();
    $('#form').show(250);
})

$(document).on('click', '#btn-estado', function() {
    var row = $(this).parents('tr');
    var data = JSON.parse($(row).attr('data-proveedor'));
    var id = data.id;
    var tipoConsulta = data.estado ? 'delete': 'restore';
    $.ajax({
        url: `${ipBack}/supplier/${tipoConsulta}Supplier/`,
        type: 'POST',
        dataType: 'JSON',
        headers: {
            'Content-Type': 'application/json'
        },
        data: JSON.stringify({'id': id}),
        success: res => {
            data.estado = !data.estado;
            $(row).attr('data-proveedor', JSON.stringify(data));
            if (data.estado) {
                $(row).find('td:eq(5)').text('ACTIVO');
                $(this)
                    .removeClass('fa-toggle-off')
                    .addClass('fa-toggle-on');
                $.notify(`El proveedor ${data.razonSocial || (data.nombres)} ha sido restaurado`, {
                    'position': 'top left',
                    'className': 'success'
                });
            } else {
                $(row).find('td:eq(5)').text('INACTIVO');
                $(this)
                    .removeClass('fa-toggle-on')
                    .addClass('fa-toggle-off');
                $.notify(`El proveedor ${data.razonSocial || (data.nombres)} ha sido desactivado`, {
                    'position': 'top left',
                    'className': 'success'
                });
            }
        },
        error: e => {
            var message = e.responseJSON ? e.responseJSON.message : `Cambiar estado: ${e.statusText}`;
            $.notify(message, {
                'position': 'top left',
                'className': 'error'
            });
        }
    })
});

$('#form form').submit(form => {
    form.preventDefault();
    var request = {};
    
    var tipoConsulta = $('#tipoConsulta').val();
    var tipoProveedor = $('#tipoProveedor').val();
    var numDoc = $('#numDoc').val();
    var apePater = $('#apePater').val();
    var apeMater = $('#apeMater').val();
    var nombres = $('#nombres').val();
    var razonSocial = $('#razonSocial').val();
    
    // INICIO GENERALES
    request.id = tipoConsulta == 'update' ? $('#id').val(): undefined;
    request.id_servicio = $('#servicios').val();
    request.tel1 = $('#tel1').val();
    request.tel2 = $('#tel2').val();
    request.correo = $('#correo').val();
    request.direccion = $('#direccion').val();
    request.id_user = tipoConsulta == 'set' ? getCookie('id'): undefined;
    // FIN GENERALES
    
    if (tipoProveedor == 'N') {
        request.apePater = apePater;
        request.apeMater = apeMater;
        request.nombres = nombres;
        request.dni = numDoc;
    } else {
        request.razonSocial = razonSocial;
        request.ruc = numDoc;
    }

    var path = tipoProveedor == 'N' ? `${tipoConsulta}PNatural/`: `${tipoConsulta}PJuridica/`;
    $.ajax({
        url: `${ipBack}/persona/${path}`,
        type: 'POST',
        dataType: 'JSON',
        headers: {
            'Content-Type': 'application/json'
        },
        data: JSON.stringify(request),
        success: res => {
            $('#cancelSupplier').click();
            getSuppliers();
            $.notify(`Guardado correctamente`, {
                'position': 'top left',
                'className': 'success'
            });
        },
        error: e => {
            var message = e.responseJSON ? e.responseJSON.message : `Guardar proveedor: ${e.statusText}`;
            $.notify(message, {
                'position': 'top left',
                'className': 'error'
            });
        }
    })
})