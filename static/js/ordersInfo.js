$(function() {
    const a = $("tbody").children();


    for (let i = 0; i < a.length; i++) {
        if (i % 4 == 0) {
            a.eq(i).addClass('warning')
        } else if (i % 4 == 1) {
            a.eq(i).addClass('danger')
        } else if (i % 4 == 2) {
            a.eq(i).addClass('info')
        } else {
            a.eq(i).addClass('success')
        }
    }

    if ($('tbody').eq(0).children() && $('tbody').eq(0).children().length > 0) {
        $("#nolist").hide();
    } else {
        $("#nolist").show();
        $("table").eq(0).hide();
    }


})