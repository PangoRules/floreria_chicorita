var menuBar = document.getElementById('menu-bar');
var nav = document.getElementById('nav');

menuBar.addEventListener('click', function(){
	nav.classList.toggle('mostrar');
});
