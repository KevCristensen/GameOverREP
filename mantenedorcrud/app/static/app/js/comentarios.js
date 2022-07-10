function commentBox(){
    let estrella = '★';

	let name = document.getElementById('name').value;
	let comment = document.getElementById('comment').value;
    let valoracion = document.getElementById('valoracion').value;

    if (name == "" || comment == "") {
        alert("Por favor introduce la informacion requerida!");
    }
    else {
        let seccion_comentarios = document.createElement('div');
        let nombre_usuario = document.createElement('h5');
        let comentario = document.createElement('p');
        let resultado = document.createElement('p');
        let division = document.createElement('hr');
        
        let txt_name = document.createTextNode(name);
        let txt_message = document.createTextNode(comment);
        let txt_valoracion = document.createTextNode(estrella.repeat(valoracion));

        nombre_usuario.appendChild(txt_name);
        resultado.appendChild(txt_valoracion);
        comentario.appendChild(txt_message);

        division.style.border = '1px solid #000';

        seccion_comentarios.appendChild(nombre_usuario);
        seccion_comentarios.appendChild(division);
        seccion_comentarios.appendChild(resultado);
        seccion_comentarios.appendChild(comentario);
        seccion_comentarios.setAttribute('class', 'pane');

        document.getElementById('result').appendChild(seccion_comentarios);

        document.getElementById('name').value= "";
        document.getElementById('comment').value= "";
        document.getElementById('valoracion').value = 5;
    }

}