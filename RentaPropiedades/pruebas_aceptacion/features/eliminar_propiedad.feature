Característica: Eliminar propiedad
    Como arrendador del sistema de rentas
    quiero eliminar una propiedad
    para dejar de publicarla y no recibir más consultas

    Escenario: El arrendador cancela la eliminación de la propiedad
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y escribe su correo "viky.aguilera@gmail.com" y su contraseña "viky1234"
    Y presiona el botón de Log in
    Y presiona el botón de mis propiedades
    Y da clic en el botón de eliminar
    Cuando presiona el botón de Cancelar
    Entonces vuelve y ve el título "Mis propiedades"
    
    Escenario: El arrendador desea eliminar una propiedad mediante URL
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y escribe su correo "viky.aguilera@gmail.com" y su contraseña "viky1234"
    Y presiona el botón de Log in
    Y presiona el botón de mis propiedades
    Cuando intento eliminar la propiedad con ID "29" mediante URL
    Entonces podra ver la confirmación "¿Estás seguro de eliminar esta propiedad?"

    Escenario: El arrendador desea eliminar una propiedad exitosamente
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y escribe su correo "viky.aguilera@gmail.com" y su contraseña "viky1234"
    Y presiona el botón de Log in
    Y presiona el botón de mis propiedades
    Y da clic en el botón de eliminar
    Cuando presiona el botón de Eliminar Propiedad
    Entonces podra ver que la propiedad con ID "29" no debería estar en Mis propiedades

    Escenario: El arrendador desea eliminar una propiedad
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y escribe su correo "viky.aguilera@gmail.com" y su contraseña "viky1234"
    Y presiona el botón de Log in
    Y presiona el botón de mis propiedades
    Y da clic en el botón de eliminar
    Cuando presiona el botón de Eliminar Propiedad
    Entonces podra ver el botón Nueva Propiedad
