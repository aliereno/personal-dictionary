$(document).ready(function () {
    $('.definition').hide();
    $('.options').hide();


    $('#newPractice').on('click', async function (e) {
        e.preventDefault();
        await addNewPractice()
    });

    jQuery(document).on('click', '.answerBtn', async function () {
        var wordId = $(this).attr('data-id')
        var wordsIdList = $(this).attr('data-words-id-list')
        var dataDefinitionId = $(this).attr('data-definition-id')
        if (wordId && dataDefinitionId) {
            var data = await fetchData('POST', '/practice/check', JSON.stringify({
                selected_word_id: wordId,
                words_id_list: wordsIdList.split(','),
                definition_id: dataDefinitionId
            }))
            if (data) {
                if (data.status == 'success') {
                    Toastify({
                        text: data.message,
                        duration: 1500,
                        newWindow: true,
                        close: true,
                        gravity: "top",
                        position: "center",
                        backgroundColor: "linear-gradient(to right, #00b09b, #96c93d)",
                        stopOnFocus: true,
                        callback: async function (r) {
                            await addNewPractice()
                        }
                    }).showToast();
                } else {
                    Toastify({
                        text: data.message,
                        duration: 1500,
                        newWindow: true,
                        close: true,
                        gravity: "top",
                        position: "center",
                        backgroundColor: "linear-gradient(to right, #b21616, #8d0909)",
                        stopOnFocus: true,
                    }).showToast();
                }
            }

        } else {
            Toastify({
                text: 'Something went wrong!',
                duration: 6000,
                newWindow: true,
                close: true,
                gravity: "bottom",
                position: "center",
                backgroundColor: "linear-gradient(to right, #b21616, #8d0909)",
                stopOnFocus: true,
            }).showToast();
        }
    });

    async function addNewPractice() {
        $('.definition').html('').hide();
        $('.options').html('').hide();
        try {
            var data = await fetchData('POST', '/practice/new')
            if (data) {
                var list = ''
                if (data && data.words.length > 0) {

                    data.words.map(function (item, index) {
                        list += `
                            <div class="col-md-4">
                                <a href="#" data-id="` + item.id + `" data-definition-id="` + data.definition.id
                            + `" data-words-id-list="` + data.words.map(value => value.id) + `" class="btn btn-primary btn-icon-split answerBtn">
                                    <span class="text">` + item.content + `</span>
                                </a>
                            </div>`
                    });
                }
                $('.options').show(50)
                $('.options').append(list)

                $('.definition').html(`
            <div class="alert alert-secondary" role="alert">
              ` + data.definition.content + `
            </div>`).show()
            }
        } catch (e) {
            Toastify({
                text: e.responseJSON.message,
                duration: 6000,
                newWindow: true,
                close: true,
                gravity: "bottom",
                position: "center",
                backgroundColor: "linear-gradient(to right, #b21616, #8d0909)",
                stopOnFocus: true,
            }).showToast();
        }
    }
});