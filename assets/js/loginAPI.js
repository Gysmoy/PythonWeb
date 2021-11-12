$('#login form').submit(e => {
    e.preventDefault();
    var username = $('#usernameLogin').val();
    var password = $('#passwordLogin').val();
    $.ajax({
        url: 'http://localhost:8000/users/validateUser/',
        method: 'POST',
        dataType: 'JSON',
        headers: {
            'Content-Type': 'application/json'
        },
        data: JSON.stringify({
            'username': username,
            'password': password,
        }),
        success: data => {
            $('#messageLogin').text(data.message);
            $('#messageLogin').show(250);
            $('#messageLogin').removeClass('danger').addClass('success');
            location.href = './client/';
        },
        error: e => {
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