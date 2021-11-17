
$('#password2Register').on ('focus',function(){
    $('#password2Register').on ('keyup',function(){
        var pw1 = $('#password1Register').val();
        var pw2 = $(this).val();
        if (pw1 === pw2){
            $('#messageSignup').attr('class', 'success');
        }else{
            $('#messageSignup').attr('class', 'danger');
        }
    })
})
$('#register form').submit(e => {
    e.preventDefault();
    var pass1 = $('#password1Register').val();
    var dni = $('#DNIRegister').val();
    var nombres = $('#lastnameRegister').val();
    var ap_paterno = $('#apellidopatRegister').val();
    var ap_materno = $('#apellidomatRegister').val();
    var fecha_nac = $('#fechanaciRegister').val();
    var sexo = $('#sexoRegister').val();
    var correo = $('#emailRegister').val();
    $.ajax({
        url: 'http://localhost:5580/users/setUser/',
        method: 'POST',
        dataType: 'JSON',
        headers: {
            'Content-Type': 'application/json'
        },
        data: JSON.stringify({
            'usuario': dni,
            'correo': correo,
            'clave': pass1,
            'dni': dni,
            'apePater': ap_paterno,
            'apeMater': ap_materno,
            'nombres': nombres,
            'sexo': sexo,
            'fec_nac': fecha_nac,
            'id_idioma': "IDI00002",
        }),
        beforeSend: function() {
        },
        success: data => {
            $('#messageSignup').text(data.message);
            $('#messageSignup').show(250);
            $('#messageSignup').removeClass('danger').addClass('success');
           /* location.href = './client/';*/
        },
        error: e => {
            var data = JSON.parse(e.responseText)
            $('#messageSignup').text(data.message);
            $('#messageSignup').show(250);
            $('#messageSignup').removeClass('success').addClass('danger');
        },
        complete: function () {
            setTimeout(function () {
                $('#messageSignup').hide(250);
            }, 2500);
        }
    })
})
