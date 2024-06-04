Característica: Eliminar reseña
    Como usuario
    Quiero eliminar la reseña que he escrito
    Para retirar mi opinion de una propiedad

    Escenario: El usuario ha cancelado la eliminación de la reseña
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "elliotnoriega@gmail.com" y su contraseña "elliot@21" 
    Y presiona el botón de Log in
    Y presiona el botón de lista de propiedades
    Y presiona el boton detalles de la propiedad "Villa bonita 2, Colinas Del Padre, Zacatecas"
    Y presiona el boton Reseñas de la propiedad
    Y presiona el boton de Eliminar reseña
    Cuando presiona el boton de Cancelar
    Entonces ve en la pagina "Ya has insertado una reseña" 
    
    Escenario: El usuario ha eliminado la reseña de forma exitosa
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "elliotnoriega@gmail.com" y su contraseña "elliot@21" 
    Y presiona el botón de Log in
    Y presiona el botón de lista de propiedades
    Y presiona el boton detalles de la propiedad "Villa bonita 2, Colinas Del Padre, Zacatecas"
    Y presiona el boton Reseñas de la propiedad
    Y presiona el boton de Eliminar reseña
    Cuando presiona el boton de eliminar confirmando su eliminación
    Entonces podra observar el boton Agregar Reseña
    
