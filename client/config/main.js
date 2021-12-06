/* Cerra modal con un botón con clase close-modal*/
$('button.close-modal').on('click', function () {
    $('a.close-modal').click();
})

// Cargar datos
$(document).on('click', '#open', function () {
    var id = $(this).attr('value');

    // Fill user data
    switch (id) {
        case '#uData-modal':
            console.log('editando datos de usuario');
            $('#password-uData').val(null);
            $('#password1-uData').val(null);
            $('#password2-uData').val(null);
            break;
        case '#pData-modal':
            var nombres = getCookie('nombres');
            var apePater = getCookie('apePater');
            var apeMater = getCookie('apeMater');
            var dni = getCookie('dni');
            var correo = getCookie('correo');
            var fec_nac = getCookie('fec_nac');
            var sexo = getCookie('sexo');
            $('#dni-pData').val(dni);
            $('#nombres-pData').val(nombres);
            $('#apePater-pData').val(apePater);
            $('#apeMater-pData').val(apeMater);
            $('#fec_nac-pData').val(fec_nac);
            $('#sexo-pData').val(sexo);
            $('#correo-pData').val(correo);
            $('#password-pData').val(null);
            break;
    }
})

$('#password-pData').on('change', function () {
    validatePassword(this);
})

$('#password-uData').on('change', function () {
    validatePassword(this);
})

function validatePassword(input) {
    var passFront = $(input).val();
    var passBack = getCookie('token');
    passFront = sha256(passFront);
    if (passFront == passBack) {
        $(input).notify(
            'Contraseña correcta',
            {
                position: 'top',
                className: 'success'
            }
        );
        return true;
    } else {
        $(input).notify(
            'Contraseña incorrecta',
            {
                position: 'top',
                className: 'error'
            }
        );
        return false;
    }
}

// Actualizar datos personales
$('#pData-modal form').submit(form => {
    form.preventDefault();

    if (validatePassword('#password-pData')) {
        var request = {};
        request.id = getCookie('id');
        request.dni = $('#dni-pData').val();
        request.nombres = $('#nombres-pData').val();
        request.apePater = $('#apePater-pData').val();
        request.apeMater = $('#apeMater-pData').val();
        request.fec_nac = $('#fec_nac-pData').val();
        request.sexo = $('#sexo-pData').val();
        request.correo = $('#correo-pData').val();
        request.clave = $('#password-pData').val();
        $.ajax({
            url: "http://127.0.0.1:8000/users/updateUserDat/",
            type: "POST",
            dataType: "JSON",
            headers: {
                'Content-Type': 'application/json'
            },
            data: JSON.stringify(request),
            success: res => {
                $('a.close-modal').click();
                $.notify(`Actualizado correctamente`, {
                    'position': 'top left',
                    'className': 'success'
                });
                setCookie('correo', request.correo);
                setCookie('dni', request.dni);
                setCookie('apePater', request.apePater);
                setCookie('apeMater', request.apeMater);
                setCookie('nombres', request.nombres);
                setCookie('sexo', request.sexo);
                setCookie('fec_nac', request.fec_nac);
            },
            error: e => {
                var message = e.responseJSON ? e.responseJSON.message : `Error al actualizar: ${e.statusText}`;
                $.notify(message, {
                    'position': 'top left',
                    'className': 'error'
                });
            }
        })
    }
});

$('#password2-uData').on('change', function() {
    var pass1 = $('#password1-uData').val();
    var pass2 = $('#password2-uData').val();
    if (pass1 === pass2) {
        $('#password2-uData').notify(
            'Contraseña coincide',
            {
                position: 'top',
                className: 'success'
            }
        );
        return true;
    } else {
        $('#password2-uData').notify(
            'Contraseña no coincide',
            {
                position: 'top',
                className: 'error'
            }
        );
        return false;
    }
})

// Actualizar datos de usuario
$('#uData-modal form').submit(form => {
    form.preventDefault();
    var pass1 = $('#password1-uData').val();
    var pass2 = $('#password2-uData').val();
    if (
        validatePassword('#password-uData') &&
        pass1 === pass2
    ) {
        var request = {};
        request.id = getCookie('id');
        request.usuario = getCookie('usuario');
        request.claveOld = getCookie('token');
        request.claveNew = pass1 || pass2;
        $.ajax({
            url: "http://127.0.0.1:8000/users/updateUserCredentials/",
            type: "POST",
            dataType: "JSON",
            headers: {
                'Content-Type': 'application/json'
            },
            data: JSON.stringify(request),
            success: res => {
                $('a.close-modal').click();
                $.notify(`Actualizado correctamente`, {
                    'position': 'top left',
                    'className': 'success'
                });
                setCookie('token', sha256(pass1 || pass2));
            },
            error: e => {
                var message = e.responseJSON ? e.responseJSON.message : `Error al actualizar: ${e.statusText}`;
                $.notify(message, {
                    'position': 'top left',
                    'className': 'error'
                });
            }
        })
    } else {
        $('#password2-pData').notify(
            'Contraseña no coincide',
            {
                position: 'top',
                className: 'error'
            }
        );
        return false;
    }
})

