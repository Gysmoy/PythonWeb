$('fom').submit(e => {
    e.preventDefault();
    var usernameLogin = $('#usernameLogin').val();
    var passwordLogin = $('#passwordLogin').val();
    console.log();
   $.ajax({
       url: '',
       type: 'POST',
       data: {
           'username':usernameLogin,
           'password':passwordLogin,

       },
       success: response => {
           var data = JSON.parse(response);
           $('#messageLogin').text(data.messager);
           $('#messageLogin').fedeIn();
           if (data.access){
               $('#messageLogin').removeClass('danger').addClas('success');
               location.href = './';
           } else{
               $('#messageLogin').removeClass('success').addClass('danger');
           }
       },
       complete: function() {
           setTimeout(function(){
               $('#messageLogin').fedeOut();
           }, 2500);
       }
   }) 

})
g