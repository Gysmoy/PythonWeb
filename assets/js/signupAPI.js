$('#dniRegister').on('keyup', function () {
    var dni = $(this).val();
    if (dni.length === 8) {
        $.ajax({
            url: 'http://34.102.135.155/data/',
            type: 'POST',
            data: {
                'tipoDocumento': 'dni',
                'numDocumento': dni
            },
            success: data => {
                var apePater = data['data']['ap_paterno'];
                var apeMater = data['data']['ap_materno'];
                var nombre = data['data']['nombres'];
                $('#apePaterRegister').val((apePater != '') ? apePater: '');
                $('#apeMaterRegister').val((apeMater != '') ? apeMater: '');
                $('#nombreRegister').val((nombre != '') ? nombre: '');
            }
        })
    } else {
        $('#apePaterRegister').val(null);
        $('#apeMaterRegister').val(null);
        $('#nombreRegister').val(null);
    }
})
$('#register > form').on('submit', e => {
    e.preventDefault();
    var lastname = $('#lastnameRegister').val();
    var name = $('#nameRegister').val();
    var email = $('#emailRegister').val();
    var password1 = $('#password1Register').val();
    var password2 = $('#password2Register').val();
    var urlAPI = $('#register > form').attr('action');
    
    $.ajax({
        url: urlAPI,
        type: 'POST',
        data: {
            'lastname': lastname,
            'name': name,
            'email': email,
            'password1': password1,
            'password2': password2
        },
        success: response => {
            var data = JSON.parse(response);
            $('#messageRegister').text(data.message);
            if (data.status === true) {
                $('#messageRegister').attr('class', null);
                $('#messageRegister').addClass('success');
            } else {
                $('#messageRegister').attr('class', null);
                $('#messageRegister').addClass('danger');
            }
        },
        error: e => {
            $('#messageRegister').text(e.statusText);
            $('#messageRegister').attr('class', null);
            $('#messageRegister').addClass('danger');
        },
        complete: function () {
            setTimeout( function() {
                $('#messageRegister').text('Ingrese sus datos para registrarlo');
                $('#messageRegister').attr('class', null);
                $('#messageRegister').addClass('info');
            }, 3000);
        }
    });
})