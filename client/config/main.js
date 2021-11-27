$('#id-data-modal').click(function() {
    var id = getCookie('id');
    var nombres = getCookie('nombres');
    var apePater = getCookie('apePater');
    var apeMater = getCookie('apeMater');
    var dni = getCookie('dni');
    var usuario = getCookie('usuario');
    var correo = getCookie('correo');
    var fec_nac = getCookie('fec_nac');
    var sexo = getCookie('sexo');

    $('#DNIRegister').val(dni);
    console.log(dni)
    alert('Hola humano');
});