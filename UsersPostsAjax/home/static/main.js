$(document).ready(function() {
    $.ajax({
        url: "/ajax/users",
        method: "GET",
    }).done(function(res) {
        $('tbody').html(res);
    })
})
$('input').keyup(function(event) {
    console.log(event);
    console.log($(this));
})
$('form').submit(function(event) {
    event.preventDefault();
    console.log($(this).serialize());
    var form = $(this);
    $.ajax({
        url: "/create",
        method: "POST",
        data: $(this).serialize()
    }).done(function(res) {
        form[0].reset();
        $('tbody').html(res);
    })
})