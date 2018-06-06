$(function() {
    $("#reg").click(function() {
        if($("#username").val().trim().length == 0) {
            alert("用户名不能为空");
        }
        if($("#password").val().trim().length == 0) {
            alert("密码不能为空");
        }
        if(($("#username").val().trim().length > 0) && ($("#password").val().trim().length > 0)) {
            setTimeout(function() {
                window.location.href = window.location.origin + '/'
            }, 3000);
            alert("注册成功，3秒后自动跳转登录页");
        }
    })
})