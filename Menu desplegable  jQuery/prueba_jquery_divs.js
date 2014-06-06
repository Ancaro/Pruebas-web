$(inicio);

function inicio () {
	// body...
	console.log("Listo!")
	$(".contenido").slideUp();
	$('.link').on('click',function() {
		$(this).siblings().slideDown();
		$(this).parent().siblings().children('.contenido').slideUp();
	});
}