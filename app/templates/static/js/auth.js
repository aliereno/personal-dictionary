$(document).ready(function () {
    var isLoggedIn = localStorage.getItem('loggedin');

    if (isLoggedIn === 1) {
        $('#sign').hide();
        $('#loginForm').hide();
        $('#signupForm').hide();
        $('#logout').show();
    } else {
        $('#sign').show();
        $('#logout').hide();
    }

    $('#loginForm').on('submit', function (e) {
        e.preventDefault();

        var username = $('#username').val();
        var password = $('#password').val();

        if (username !== "" && password !== "") {
            $.ajax({
                method: "POST",
                url: '/login',
                contentType: 'application/json;charset=UTF-8',
                data: JSON.stringify({'username': username, 'password': password}),
                dataType: "json",
                success: function (data) {
                    if (data && data.message) {
                        Toastify({
                            text: data.message,
                            duration: 1500,
                            newWindow: true,
                            close: true,
                            gravity: "top",
                            position: "center",
                            backgroundColor: "linear-gradient(to right, #00b09b, #96c93d)",
                            stopOnFocus: true,
                            callback: function (r) {
                                window.location = '/dashboard'
                            }
                        }).showToast();
                    }
                },
                statusCode: {
                    400: function (err) {
                        if (err && err.responseJSON.error) {
                            Toastify({
                                text: err.responseJSON.error,
                                duration: 6000,
                                newWindow: true,
                                close: true,
                                gravity: "top",
                                position: "center",
                                backgroundColor: "linear-gradient(to right, #b21616, #8d0909)",
                                stopOnFocus: true,
                            }).showToast();
                        }
                    }
                },
                error: function (err) {
                    console.log(err);
                }
            });
        } else {
            Toastify({
                text: "Username or Password can not be null!",
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
    $('#signupForm').on('submit', function (e) {
        e.preventDefault();

        var username = $('#username').val();
        var password = $('#password').val();

        if (username !== "" && password !== "") {
            $.ajax({
                method: "POST",
                url: '/signup',
                contentType: 'application/json;charset=UTF-8',
                data: JSON.stringify({'username': username, 'password': password}),
                dataType: "json",
                success: function (data) {
                    if (data && data.message) {
                        Toastify({
                            text: data.message,
                            duration: 1500,
                            newWindow: true,
                            close: true,
                            gravity: "top",
                            position: "center",
                            backgroundColor: "linear-gradient(to right, #00b09b, #96c93d)",
                            stopOnFocus: true,
                            callback: function (r) {
                                window.location = '/login'
                            }
                        }).showToast();
                    }
                },
                statusCode: {
                    400: function (err) {
                        if (err && err.responseJSON.error) {
                            Toastify({
                                text: err.responseJSON.error,
                                duration: 6000,
                                newWindow: true,
                                close: true,
                                gravity: "top",
                                position: "center",
                                backgroundColor: "linear-gradient(to right, #b21616, #8d0909)",
                                stopOnFocus: true,
                            }).showToast();
                        }
                    }
                },
                error: function (err) {
                    console.log(err);
                }
            });
        } else {
            Toastify({
                text: "Username or Password can not be null!",
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

    $('#logout').on('click', function (e) {
        e.preventDefault();

        $.ajax({
            url: '/logout',
            dataType: "json",
            success: function (data) {
                localStorage.setItem('loggedin', 0);
                $('#sign').show();
                $('#logout').hide();
                $('#msg').html('<span style="color: green;">You are logged off</span>');
            },
            error: function (err) {
                console.log(err);
            }
        });
    });
});