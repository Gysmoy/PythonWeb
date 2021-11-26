var providers = [];
$(document).ready(function() {
    /*var usuario = getCookie('usuario');
    $.ajax({
        url: ipgeneral + '/providers/getProviders',
        type: 'GET',
        success: res => {
            providers = res.data;
        }
    })*/
    $.ajax({
        url: ipBack + '/services/getServices/',
        type: 'GET',
        dataType: 'JSON',
        success: res => {
            console.log(res.data);
            res.data.forEach(s => {
                var id = s.id;
                var servicio = s.servicio;
                if (s.estado){
                    $('#servicios').append(`
                    <option value="${id}" label="${servicio}">${servicio}</option>
                    `);
                }
            });
        }
    })
})
