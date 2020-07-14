$(document).ready(function() {
    $.ajax({
        url: '/fetch',
        method: 'GET'
    }).done(function(response) {
        $('tbody').html(response)
    })
})
$("input").keyup(function(event) {
    $.ajax({
        url: '/email_check',
        method: 'POST',
        data: {
            value: event.target.value,
            fieldName: event.target.name,
            csrfmiddlewaretoken: getCookie('csrftoken')
        }
    }).done(function(response) {
        console.log(response);
        $("#error").html(response);
    })
})
$('form').submit(function(event) {
    event.preventDefault();
    var form = $(this);
    $.ajax({
        url: '/create',
        method: 'POST',
        data: form.serialize()
    }).done(function(response) {
        $('tbody').html(response)
    })
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
