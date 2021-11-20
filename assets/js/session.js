function activeSession(data) {
    setCookie('id', data.id);
    setCookie('usuario', data.usuario);
    setCookie('token', data.clave);
    setCookie('correo', data.correo);
    setCookie('dni', data.dni);
    setCookie('apePater', data.apePater);
    setCookie('apeMater', data.apeMater);
    setCookie('nombres', data.nombres);
    setCookie('sexo', data.sexo);
    setCookie('fec_nac', data.fec_nac);
    setCookie('id_idioma', data.id_idioma);
}

function destroySession() {
    deleteCookie();
    location.href = '/';
}