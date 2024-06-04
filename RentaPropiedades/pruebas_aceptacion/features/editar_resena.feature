Característica: Crear reseña
    Como Usuario
    Quiero editar una reseña existente sobre una propiedad
    para actualizar mi opinion o corregir información

    Escenario: El usuario edito su descripcion de la reseña de forma exitosa
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "elliotnoriega@gmail.com" y su contraseña "elliot@21" 
    Y presiona el botón de Log in
    Y presiona el botón de lista de propiedades
    Y presiona el boton detalles de la propiedad "Villa bonita 2, Colinas Del Padre, Zacatecas"
    Y presiona el boton Reseñas de la propiedad
    Y presiona el boton de Editar reseña
    Y modifica la descripción con el texto "Me hospede en esta propiedad un año, y el trato y servicios fuerón excepcionales, 100% recomendado, Un saludo al ingeniero"
    Cuando presiona el boton Guardar
    Entonces ve la reseña modificada con la descripción: "Me hospede en esta propiedad un año, y el trato y servicios fuerón excepcionales, 100% recomendado, Un saludo al ingeniero" 

    Escenario: El usuario edito su calificación de la reseña de forma exitosa
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "elliotnoriega@gmail.com" y su contraseña "elliot@21" 
    Y presiona el botón de Log in
    Y presiona el botón de lista de propiedades
    Y presiona el boton detalles de la propiedad "Villa bonita 2, Colinas Del Padre, Zacatecas"
    Y presiona el boton Reseñas de la propiedad
    Y presiona el boton de Editar reseña
    Y modifica la calificación asignando "3" estrellas a la reseña
    Cuando presiona el boton Guardar
    Entonces ve la reseña modificada con la calificacion de "3" estrellas

    Escenario: El usuario edito su descripción de la reseña dejandola vacia
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "elliotnoriega@gmail.com" y su contraseña "elliot@21" 
    Y presiona el botón de Log in
    Y presiona el botón de lista de propiedades
    Y presiona el boton detalles de la propiedad "Villa bonita 2, Colinas Del Padre, Zacatecas"
    Y presiona el boton Reseñas de la propiedad
    Y presiona el boton de Editar reseña
    Y modifica la descripción dejandola vacia
    Cuando presiona el boton Guardar
    Entonces ve el mensaje en el campo descripcion "Completa este campo"

    Escenario: El usuario cancelara la edición de la reseña
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "elliotnoriega@gmail.com" y su contraseña "elliot@21" 
    Y presiona el botón de Log in
    Y presiona el botón de lista de propiedades
    Y presiona el boton detalles de la propiedad "Villa bonita 2, Colinas Del Padre, Zacatecas"
    Y presiona el boton Reseñas de la propiedad
    Y presiona el boton de Editar Reseña
    Cuando presiona el boton de Cancelar
    Entonces ve en la pagina "Ya has insertado una reseña" 

    