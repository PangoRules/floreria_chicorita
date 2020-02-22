var form_fields = document.getElementsByTagName('input');
form_fields[2].placeholder='Nombre de usuario..';
form_fields[3].placeholder='Correo..';
form_fields[4].placeholder='Contraseña..';
form_fields[5].placeholder='Escriba la contraseña de nuevo..'


for (var field in form_fields){	
	form_fields[field].className += ' form-control'
}