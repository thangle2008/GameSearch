$(document).ready(function() {
	// add bootstrap classes to giantbomb-generated HTML tags
	$('.giantbomb-data figure').addClass('figure text-center');
	$('.giantbomb-data figure img').addClass('figure-img img-fluid rounded');
	$('.giantbomb-data figure img').css({'margin' : '0 auto'});
	$('.giantbomb-data figure figcaption').addClass('figure-caption');
	$('.giantbomb-data table').addClass('table table-striped');
	$('.giantbomb-data p').css({'font-weight': '300', 'line-height': '1.5', 'font-size' : '14pt'});

	// add line break after each figure
	$('.giantbomb-data figure figcaption').after('<br>');
});