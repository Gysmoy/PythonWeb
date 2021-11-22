var providers = [];
$(document).ready(function() {
    var usuario = getCookie('usuario');
    $.ajax({
        url: ipgeneral + '/providers/getProviders',
        type: 'GET',
        success: res => {
            providers = res.data;
        }
    })
})