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
        }
    });
})