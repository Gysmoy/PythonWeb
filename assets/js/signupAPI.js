$('#dniRegister').on('keyup', function () {
    var dni = $(this).val();
    if (dni.length === 8) {
        $.ajax({
            url: 'https://oim.mapfre.com.pe/oim_polizas/api/form/person/equifax',
            type: 'POST',
            headers: {
                'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJVc2VyVHlwZSI6IjMiLCJVc2VyU3ViVHlwZSI6IjMiLCJMb2dpblVzZXJOYW1lIjoiNDA2NDAxNjkiLCJVc2VyTmFtZSI6IkxJTFkgT0xJVkFSRVMgSEVSUkVSQSIsIkNsaWVudFByb2ZpbGUiOiIwIiwiVXNlclByb2ZpbGUiOiIiLCJBZ2VudE5hbWUiOiJHRVJFTkNJQSBERSBSSUVTR09TIEFTRVMgWSBDIiwiQWdlbnRJRCI6Ijg3MCIsIkRvY3VtZW50TnVtYmVyIjoiNDA2NDAxNjkiLCJSdWNOdW1iZXIiOiIyMDI1ODM0MjI0MSIsIlVzZXJFbWFpbCI6IkxPTElWQVJFU0BHRVJFTkNJQURFUklFU0dPUy5DT00iLCJUb2tlbk1hcGZyZSI6IiIsIlJvbGVDb2RlIjoiQ09SUkVET1IiLCJSb2xlTmFtZSI6IkNPUlJFRE9SIC0gIiwiT2ZmaWNlQ29kZSI6IjAiLCJVcmxSZWRpcmVjdCI6Imh0dHBzOi8vb2ltLm1hcGZyZS5jb20ucGUvT0lNQ09SUi9JbmljaW9Db3JyLmFzcHg_cGFyYW0xPTQwNjQwMTY5XHUwMDI2cGFyYW0yPUROSVx1MDAyNnBhcmFtMz3CrsODbsOTwq_DlVPDrcOrw45cdTAwMjZwYXJhbTQ9MCIsIkZsYWdVc2VyQnlQYXNzIjoiUyIsIklDb2RlTXgiOiIiLCJEb2N1bWVudFR5cGUiOiJETkkiLCJQZXJmaWxJZCI6IiIsIkdlc3RvcklkIjoiMCIsIkdlc3Rvck5hbWUiOiIiLCJQZXJzb25JZCI6IjU2NzQwIiwiVXNlcklkIjoiMzI0NjYiLCJDb21wYW55SWQiOiI1MTA5IiwiQ29tcGFueU5hbWUiOiJHRVJFTkNJQSBERSBSSUVTR09TIEFTRVMgWSBDIiwiVXNlckFkbWluUmVndWxhciI6IlUiLCJJc0F1dG9TZXJ2aWNlIjoiRmFsc2UiLCJMb2dpbkRhdGUiOiI2Mzc2NDE4NTIyMDAwMDAwMDAiLCJJc0VuY3J5cHQiOiJUcnVlIiwiaXNzIjoiaHR0cDovL2p3dGF1dGh6c3J2LmF6dXJld2Vic2l0ZXMubmV0IiwiYXVkIjoiMDk5MTUzYzI2MjUxNDliYzhlY2IzZTg1ZTAzZjAwMjIiLCJleHAiOjE2Mjg2OTI4MjAsIm5iZiI6MTYyODYwNjQyMH0.TuFPaKoF5GgibVE1iRS-l4-AnEI8bf0it7JiJxYvcuU',
            },
            data: {
                'applicationCode': 'AUTOMOVILES',
                'tipoDocumento': 'DNI',
                'codigoDocumento': dni,
                'codigoCompania': 1
            },
            success: data => {
                var apePater = data['Data']['ApellidoPaterno'];
                var apeMater = data['Data']['ApellidoMaterno'];
                var nombre = data['Data']['Nombre'];
                $('#apePaterRegister').val((apePater != '') ? apePater: '');
                $('#apeMaterRegister').val((apeMater != '') ? apeMater: '');
                $('#nombreRegister').val((nombre != '') ? nombre: '');
            }
        })
    } else {
        $('#apePaterRegister').val(null);
        $('#apeMaterRegister').val(null);
        $('#nombreRegister').val(null);
    }
})
$('#register > form').on('submit', e => {
    e.preventDefault();
    var lastname = $('#lastnameRegister').val();
    var name = $('#nameRegister').val();
    var email = $('#emailRegister').val();
    var password1 = $('#password1Register').val();
    var password2 = $('#password2Register').val();
    var urlAPI = $('#register > form').attr('action');
    
    $.ajax({
        url: urlAPI,
        type: 'POST',
        data: {
            'lastname': lastname,
            'name': name,
            'email': email,
            'password1': password1,
            'password2': password2
        },
        success: response => {
            var data = JSON.parse(response);
            $('#messageRegister').text(data.message);
            if (data.status === true) {
                $('#messageRegister').attr('class', null);
                $('#messageRegister').addClass('success');
            } else {
                $('#messageRegister').attr('class', null);
                $('#messageRegister').addClass('danger');
            }
        },
        error: e => {
            $('#messageRegister').text(e.statusText);
            $('#messageRegister').attr('class', null);
            $('#messageRegister').addClass('danger');
        },
        complete: function () {
            setTimeout( function() {
                $('#messageRegister').text('Ingrese sus datos para registrarlo');
                $('#messageRegister').attr('class', null);
                $('#messageRegister').addClass('info');
            }, 3000);
        }
    });
})