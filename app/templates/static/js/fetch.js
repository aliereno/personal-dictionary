async function fetchData(method, url, payload) {
    return $.ajax({
        method: method,
        url: url,
        contentType: 'application/json;charset=UTF-8',
        data: payload,
        dataType: "json",
        success: function (data) {
            return data
        },
        error: function (err) {
            throw err
        }
    });
}