$(document).ready(function() {
    $('#btn_translate').click(function() {
        const languageCode = $('#language_code').val();
        const url = 'https://fourtonfish.com/hellosalut/?lang=' + languageCode;
        $.get(url, function(data) {
            $('#hello').text(data.hello);
        });
    });

    $('#language_code').keypress(function(event) {
        if (event.keyCode === 13) {
            $('#btn_translate').click();
        }
    });
});
