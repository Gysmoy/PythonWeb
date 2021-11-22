function setCookie(key, value) {
    document.cookie = `${key}=${value}; `;
}
function getCookie(key) {
    var name = key + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ')
            c = c.substring(1);
        if (c.indexOf(name) == 0)
            return c.substring(name.length, c.length);
    }
    return "";
}
function deleteCookie() {
    document.cookie = "id=; expires=Thu, 01 Jan 1970 00:00:00 UTC";
    document.cookie = "usuario=; expires=Thu, 01 Jan 1970 00:00:00 UTC";
    document.cookie = "correo=; expires=Thu, 01 Jan 1970 00:00:00 UTC";
    document.cookie = "token=; expires=Thu, 01 Jan 1970 00:00:00 UTC";
    document.cookie = "dni=; expires=Thu, 01 Jan 1970 00:00:00 UTC";
    document.cookie = "apePater=; expires=Thu, 01 Jan 1970 00:00:00 UTC";
    document.cookie = "apeMater=; expires=Thu, 01 Jan 1970 00:00:00 UTC";
    document.cookie = "nombres=; expires=Thu, 01 Jan 1970 00:00:00 UTC";
    document.cookie = "sexo=; expires=Thu, 01 Jan 1970 00:00:00 UTC";
    document.cookie = "fec_nac=; expires=Thu, 01 Jan 1970 00:00:00 UTC";
    document.cookie = "id_idioma=; expires=Thu, 01 Jan 1970 00:00:00 UTC";
}