$(inicio);

function inicio () {
    	 botonBuscar = $('#botonBuscar');
    	 botonBuscar.on('click',buscarArtista);
}    	 

function buscarArtista () {
	var nombreArtista = $('#nombreArtista').val(),
		api_key       = 'c59f54dd152806116d58a6350d442d10';

	console.log('El artista que busco es: '+nombreArtista);

	$.ajax({
		data:{
			artist:nombreArtista,
			api_key:api_key,
			format:'json',
			method:'artist.getinfo'
		},
		url:'http://ws.audioscrobbler.com/2.0/'
	})
	.done(presentarArtista);
}

function presentarArtista (datosArtista) {
	var artista   = datosArtista.artist;
	var html      = '',
		resultado = $('#resultado');

	html += '<h2>'+artista.name+'</h2>';
	html += '<img src="' +artista.image[artista.image.length - 1]['#text']+ '">';
	html += '<p>'+artista.bio.summary+'</p>';
	console.log(html);
	resultado.html( html );
}