Característica: Ver detalles de los estudiantes interesados
    Como arrendador del sistema de rentas
    quiero ver detalles de los estudiantes interesados en mi propiedad
    para evaluar mejor a los posibles inquilinos

    Escenario: El arrendador puede ver información detallada de un interesado
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y escribe su correo "viky.aguilera@gmail.com" y su contraseña "viky1234"
    Y presiona el botón de Log in
    Y presiona el botón de mis propiedades
    Y presiona el botón de Detalles
    Y da clic en el botón de Interesados
    Cuando presiona el botón de Ver Perfil de algún interesado
    Entonces puede ver la información del interesado seleccionado

    Escenario: El arrendador puede ver información detallada de un interesado 2.0
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y escribe su correo "viky.aguilera@gmail.com" y su contraseña "viky1234"
    Y presiona el botón de Log in
    Y presiona el botón de mis propiedades
    Y presiona el botón de Detalles
    Y da clic en el botón de Interesados
    Cuando presiona el botón de Ver Perfil del interesado "77"
    Entonces puede ver la información del interesado con ID "77"