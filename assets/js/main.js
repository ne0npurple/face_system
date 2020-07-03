$(document).ready(function() {

	$('#nav_headers span').mouseenter(function() {
		var elem_class = $(this).attr('class');
		var elem_width = $(this).css('width');
		var matching_ul = $('ul.' + elem_class);
		matching_ul.css('visibility', 'visible');
		matching_ul.css('min-width', elem_width);
	}).mouseleave(function() {
		var elem_class = $(this).attr('class');
		$('ul.' + elem_class).css('visibility', 'hidden');
	});

	$('#nav_menus ul').mouseenter(function() {
		$(this).css('visibility', 'visible');
	}).mouseleave(function() {
		$(this).css('visibility', 'hidden');
	});
});