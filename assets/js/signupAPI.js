function validatePWD1() {
    var pwd1 = $('#password1Register').val();
    var pwd2 = $('#password2Register').val();
    if (pwd1.length < 8) {
        $('#messageRegister').attr('class', 'danger').text('Las contraseña debe contener mas de 8 caracteres');
    } else {
        $('#messageRegister').attr('class', 'success').text('Correcto: contraseña valida');

        if (pwd2.length > 0) validatePWD2();
    }
}
function validatePWD2() {
    var pwd1 = $('#password1Register').val();
    var pwd2 = $('#password2Register').val();
    if (pwd1 === pwd2) {
        $('#messageRegister').attr('class', 'success').text('Correcto:  las contraseñas coinciden');
    } else {
        $('#messageRegister').attr('class', 'danger').text('Las contraseñas deben coincidir');
    }
}

$('#password1Register').on('keyup', validatePWD1);
$('#password2Register').on('keyup', validatePWD2);

$('#register > form').on('submit', e => {
    e.preventDefault();
    var correo = $('#emailRegister').val();
    var usuario = (/^([^]+)@(\w+).(\w+)$/.exec(correo))[1].substr(0, 16);
    var clave1 = $('#password1Register').val();
    var clave2 = $('#password2Register').val();
    var dni = $('#DNIRegister').val();
    var apePater = $('#apellidopatRegister').val();
    var apeMater = $('#apellidomatRegister').val();
    var nombres = $('#lastnameRegister').val();
    var sexo = $('#sexoRegister').val();
    var fec_nac = $('#fechanaciRegister').val();
    var id_idioma = 1;
    if (clave1 != clave2)
        validatePWD2();
    else {
        var clave = clave1 || clave2;
        $.ajax({
            url: 'http://127.0.0.1:8000/users/setUser/',
            type: 'POST',
            dataType: 'JSON',
            headers: {
                'Content-Type': 'application/json'
            },
            data: JSON.stringify({ usuario, correo, clave, dni, apePater, apeMater, nombres, sexo, fec_nac, id_idioma }),
            success: data => {
                $('#messageLogin').text(data.message);
                $('#messageLogin').show(250);
                $('#messageLogin').removeClass('danger').addClass('success');
                location.href = './client/';
            },
            error: e => {
                var data = JSON.parse(e.responseText)
                $('#messageLogin').text(data.message);
                $('#messageLogin').show(250);
                $('#messageLogin').removeClass('success').addClass('danger');
            },
            complete: function () {
                setTimeout(function () {
                    $('#messageLogin').hide(250);
                }, 2500);
            }
        });
    }
})