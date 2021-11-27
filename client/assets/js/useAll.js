function setMenu() {
    var path = location.pathname.split('/');
    var retros = {
        '3': './',
        '4': '../',
        '5': '../../'
    }
    var retro = retros[path.length];
    $('#menu ul').html(`
        <li><a href="${retro}">Inicio</a></li>
        <li><a href="${retro}paymentChron/">Cronograma de pagos</a></li>
        <li><a href="${retro}providerFlow/">Flujo de proveedores</a></li>
        <li><a href="${retro}providerList/">Lista de proveedores</a></li>
        <li><a href="${retro}config/">Configuración</a></li>
        <li><a href="#" onclick="destroySession()">Cerrar sesión</a></li>
    `);
}
setMenu();