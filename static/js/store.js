$(function () {
    if ($("#flist").eq(0).children() && $("#flist").eq(0).children().length > 0) {
        $("#nolist").hide();
    } else {
        $("#nolist").show();
    }
})