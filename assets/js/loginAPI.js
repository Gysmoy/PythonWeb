$('#login form').submit(e => {
    e.preventDefault();
    var username = $('#usernameLogin').val();
    var password = $('#passwordLogin').val();
    $.ajax({
<<<<<<< HEAD
        url:'http://127.0.0.1:8000/users/validateUser/',
=======
        url: ipBack + '/users/validateUser/',
>>>>>>> 6aa5183369a22d729ac566d7b9b046a7b2422e0c
        method: 'POST',
        dataType: 'JSON',
        headers: {
            'Content-Type': 'application/json'
        },
        data: JSON.stringify({
            'username': username,
            'password': password,
        }),
        beforeSend: function() {
        },
        success: data => {
            $('#messageLogin').text(data.message);
            $('#messageLogin').show(250);
            $('#messageLogin').removeClass('danger').addClass('success');
            activeSession(data.data);
            location.href = './client/';
        },
        error: e => {
            console.log(e)
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
    })
})
$('a[href="#login"]').click(function() {
    deleteCookie();
})