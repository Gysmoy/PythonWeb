function fillUser(){
    var nombres = getCookie('nombres');
    var apePater = getCookie('apePater');
    var apeMater = getCookie('apeMater');
    var dni = getCookie('dni');
    var correo = getCookie('correo');
    var fec_nac = getCookie('fec_nac');
    var sexo = getCookie('sexo');
    
    $('#DNIRegister').val(dni);
    $('#lastnameRegister').val(nombres);
    $('#apellidopatRegister').val(apePater);
    $('#apellidomatRegister').val(apeMater);
    $('#fechanaciRegister').val(fec_nac);
    $('#sexoRegister').val(sexo);
    $('#emailRegister').val(correo);
}

$('#act-user-modal').click(function() {
   fillUser()
}); 

$('#passwordValActDat').keyup(function () { 
    $('.close-modal').attr('id','cerrar_modal')
    var request = {};
    var pass = getCookie('token');
    var clave = $('#passwordValActDat').val()
    var claveHash = sha256(clave)

    if (pass === claveHash){

        $('#messageUpUsDat').text('Contraseña correcta').css({'display':'block'}).attr('class', 'success')
        
        $('#data-modal form').submit(form  => { 
            form.preventDefault();

            request.id = getCookie('id');

            request.correo = $('#emailRegister').val();
            request.dni = $('#DNIRegister').val();
            request.apePater = $('#apellidopatRegister').val();
            request.apeMater = $('#apellidomatRegister').val();
            request.nombres = $('#lastnameRegister').val();
            request.sexo = $('#sexoRegister').val();
            request.fec_nac = $('#fechanaciRegister').val();

            request.clave = pass;

            $.ajax({
                type: "POST",
                url: "http://127.0.0.1:8000/users/updateUserDat/",
                dataType: "JSON",
                headers: {
                    'Content-Type': 'application/json'
                },
                data: JSON.stringify(request),
                success: res => {
                    
                    $('#cerrar-wind-up-da-us').click();

                    $.notify(`Actualizado correctamente`, {
                        'position': 'top left',
                        'className': 'success'
                    });

                    // ELIMINADO CONTRASEÑA DEL FORM
                    $('#passwordValActDat').val('')

                    // ACTUALIZANDO COOKIES
                    deleteCookie();

                    setCookie('correo',request.correo)
                    setCookie('dni',request.dni)
                    setCookie('apePater',request.apePater)
                    setCookie('apeMater',request.apeMater)
                    setCookie('nombres',request.nombres)
                    setCookie('sexo',request.sexo)
                    setCookie('fec_nac',request.fec_nac)


                },
                error: e => {
                    var message = e.responseJSON ? e.responseJSON.message : `Actualizar Datos de Usuario: ${e.statusText}`;
                    $.notify(message, {
                        'position': 'top left',
                        'className': 'error'
                    });
                }
            });
        });
    }else{
        $('#messageUpUsDat').text('Contraseña incorrecta').css({'display':'block'}).attr('class', 'danger')
    }
});

