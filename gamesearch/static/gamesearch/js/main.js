$(document).ready(function() {
    $('.box-image-text').matchHeight();

    $('.rating').each(function() {
        var thisRating = $(this);

        thisRating.raty({
            path: 'https://cdnjs.cloudflare.com/ajax/libs/raty/2.7.1/images',
            click: function(score) {
                $.ajax({
                    method: 'POST',
                    url: window.location.href,
                    data: {'game_id': thisRating.data('id'), 'score': score}
                });
            }
        })
    })
});