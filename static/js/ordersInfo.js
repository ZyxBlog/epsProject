$(function() {
    for(let i = 0; i < $('.total').length; i++) {
        const t = $('.total').eq(i).prev().prev().html() * $('.total').eq(i).prev().html();
        $(".total").eq(i).html(t)
    }

    const a = $("tbody").children();
    for(let i = 0; i < a.length; i++) {
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
})