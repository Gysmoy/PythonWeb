$(document).ready(function() {
    $('.buttonActions').hide();
})

$('div.box h2').click(async function() {
    var buttonActions = $(this).parent().children('.buttonActions');
    if (buttonActions.is(':visible')) {
        buttonActions.hide(250);
    } else {
        $('div.box .buttonActions').hide(250);
        $(this).parent().children('.buttonActions').show(250);
    }
})