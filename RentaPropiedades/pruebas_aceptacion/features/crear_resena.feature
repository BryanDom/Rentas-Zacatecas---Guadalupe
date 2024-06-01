Característica: Crear reseña
    Como Usuario
    Quiero crear una reseña sobre una propiedad
    para compartir mi experiencia con otros estudiantes

    Escenario: El usuario cancela la creación de la reseña
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "elliotnoriega@gmail.com" y su contraseña "elliot@21" 
    Y presiona el botón de Log in
    Y presiona el botón de lista de propiedades
    Y presiona el boton detalles de la propiedad "Del Angel 12, Centro Sct Zacatecas, Zacatecas"
    Y presiona el boton Reseñas de la propiedad
    Y presiona el boton Agregar Reseña
    Y escribe en la descripción "100% recomendado"
    Cuando presiona el boton de Cancelar
    Entonces podra observar el boton Agregar Reseña

    Escenario: El usuario puede crear una reseña de forma exitosa
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "elliotnoriega@gmail.com" y su contraseña "elliot@21" 
    Y presiona el botón de Log in
    Y presiona el botón de lista de propiedades
    Y presiona el boton detalles de la propiedad "Del Angel 12, Centro Sct Zacatecas, Zacatecas"
    Y presiona el boton Reseñas de la propiedad
    Y presiona el boton Agregar Reseña
    Y escribe en la descripción "Me hospede en esta propiedad un año, y el trato y servicios fuerón excepcionales, 100% recomendado"
    Y selecciona como calificación "5" estrellas
    Cuando presiona el boton Guardar
    Entonces ve en la pagina "Ya has insertado una reseña" 

    Escenario: El usuario no puede crear una reseña de nuevo a una propiedad
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "elliotnoriega@gmail.com" y su contraseña "elliot@21" 
    Y presiona el botón de Log in
    Y presiona el botón de lista de propiedades
    Y presiona el boton detalles de la propiedad "Del Angel 12, Centro Sct Zacatecas, Zacatecas"
    Cuando presiona el boton Reseñas de la propiedad
    Entonces ve en la pagina "Ya has insertado una reseña" 

    Escenario: El usuario no puede crear una reseña sin descripcion
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "elliotnoriega@gmail.com" y su contraseña "elliot@21" 
    Y presiona el botón de Log in
    Y presiona el botón de lista de propiedades
    Y presiona el boton detalles de la propiedad "Venustiano Carranza 25, Ayuntamiento, Zacatecas"
    Y presiona el boton Reseñas de la propiedad
    Y presiona el boton Agregar Reseña
    Y selecciona como calificación "4" estrellas
    Cuando presiona el boton Guardar
    Entonces ve el mensaje en el campo descripcion "Completa este campo"

    Escenario: El usuario no puede crear una reseña sin calificacion
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "elliotnoriega@gmail.com" y su contraseña "elliot@21" 
    Y presiona el botón de Log in
    Y presiona el botón de lista de propiedades
    Y presiona el boton detalles de la propiedad "Venustiano Carranza 25, Ayuntamiento, Zacatecas"
    Y presiona el boton Reseñas de la propiedad
    Y presiona el boton Agregar Reseña
    Y escribe en la descripción "100% recomendado"
    Cuando presiona el boton Guardar
    Entonces ve el mensaje de error "Por favor, selecciona una calificación."
