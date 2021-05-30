$(document).ready(function () {
    $('.add-button').hide();
    $('.loading').hide();

    $('#searchBtn').on('click', async function (e) {
        e.preventDefault();

        var word = $('#word').val();
        $('.loading').show();
        $('.add-button').hide();
        $('.definitions').html('')
        var list = ''
        if (word !== "") {
            try {
                var data = await fetchData('POST', '/search', JSON.stringify({'search': word}))
                $('.loading').hide();
                if (data && data.definitions.length > 0) {
                    data.definitions.map(function (data, index) {
                        list += '<li class="list-group-item">' + data.content + '</li>'
                    });
                    $('.add-button').attr('data-id', data.id);
                    $('.add-button').show(300);
                }
                $('.definitions').append(list)
            } catch (e) {
                $('.loading').hide();
                $('.definitions').append('<div class="alert alert-danger">No records found!</div>')
            }
        } else {
            Toastify({
                text: "Word can not be null!",
                duration: 6000,
                newWindow: true,
                close: true,
                gravity: "top",
                position: "center",
                backgroundColor: "linear-gradient(to right, #b21616, #8d0909)",
                stopOnFocus: true,
            }).showToast();
        }
    });

    $('#addBtn').on('click', async function (e) {
        e.preventDefault();
        try {
            var data = await fetchData('POST', '/dictionary', JSON.stringify({'word_id': $(this).attr('data-id')}))
            if (data) {
                Toastify({
                    text: "Word added successfuly!",
                    duration: 2000,
                    newWindow: true,
                    close: true,
                    gravity: "top",
                    position: "center",
                    backgroundColor: "linear-gradient(to right, #00b09b, #96c93d)",
                    stopOnFocus: true,
                }).showToast();
            }
        } catch (e) {
                Toastify({
                    text: "Something went wrong!",
                    duration: 2000,
                    newWindow: true,
                    close: true,
                    gravity: "top",
                    position: "center",
                    backgroundColor: "linear-gradient(to right, #b21616, #8d0909)",
                    stopOnFocus: true,
                }).showToast();
        }
    });
});