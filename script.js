$(document).ready(function() {
    $.get('/apod', function(data) {
        $('#apod-image').attr('src', data.url);
        $('#apod-title').text(data.title);
        $('#apod-date').text(data.date);
        $('#apod-explanation').text(data.explanation);
    });
});
