Característica: Visualizar lista de propiedades
    Como usuario del sistema de rentas
    quiero ver la lista de propiedades disponibles
    para encontrar una propiedad que cumpla con mis necesidades.


    Escenario: El usuario puede ver propiedades de manera exitosamente
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "estudiante@ejemplo.com" y su contraseña "1234" 
    Y presiona el botón de Log in
    Cuando presiona el botón de lista de propiedades 
    Entonces puede ver una lista de propiedades con información.

    Escenario: El usuario puede ver los detalles de una propiedad especifica
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "estudiante@ejemplo.com" y su contraseña "1234"
    Y presiona el botón de Log in
    Y presiona el botón de lista de propiedades 
    Cuando presiona el botón de detalles de una propiedad
    Entonces puede ver la información de la propiedad seleccionada.

    Escenario: El usuario puede ver los detalles del arrendador de una propiedad especifica
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "estudiante@ejemplo.com" y su contraseña "1234"
    Y presiona el botón de Log in
    Y presiona el botón de lista de propiedades 
    Y presiona el botón de detalles de una propiedad
    Cuando presiona el botón de información del arrendador
    Entonces puede ver la información del arrendador de la propiedad seleccionada.

    Escenario: El usuario puede destacar una propiedad como favorita
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "estudiante@ejemplo.com" y su contraseña "1234"
    Y presiona el botón de Log in
    Y presiona el botón de lista de propiedades 
    Y presiona el botón de detalles de una propiedad
    Y presiona el botón de agregar a favoritos
    Cuando presiona el botón de ver favoritos
    Entonces puede ver la propiedad que agrego a favoritos.

    Escenario: El usuario puede marcar interes en una propiedad
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "estudiante@ejemplo.com" y su contraseña "1234"
    Y presiona el botón de Log in
    Y presiona el botón de lista de propiedades 
    Y presiona el botón de detalles de una propiedad
    Cuando presiona el botón de inscribirme a la lista de interesados
    Entonces puede ver el mensaje de que ya esta inscrito a la lista.

    Escenario: El arrendador puede ver la lista de intersados en su propiedad
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "ejemplo@dominio.com" y su contraseña "1234" 
    Y presiona el botón de Log in
    Y presiona el botón de lista de mis propiedades 
    Y presiona el botón de detalles propiedad
    Cuando presiona el botón de interesados
    Entonces puede ver los interesados en su propiedad.