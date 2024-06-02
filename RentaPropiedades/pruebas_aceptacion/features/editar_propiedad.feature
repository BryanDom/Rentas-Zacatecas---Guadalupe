Característica: Editar propiedad
    Como arrendador 
    quiero editar una propiedad exitosamente
    para mantener la información actualizada

    Escenario: El arrendador edita información de una propiedad correctamente
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y escribe su correo "viky.aguilera@gmail.com" y su contraseña "viky1234"
    Y presiona el botón de Log in
    Y presiona el botón de mis propiedades
    Y da clic en el botón de Editar 
    Y actualiza el precio "5200"
    Y actualiza el tipo de propiedad a "1"
    Y selecciona otra imagen de la propiedad "imagenes_pruebas\Departamento_03.jpg"
    Cuando presiona en el botón Guardar cambios
    Entonces puede ver el tipo de propiedad "Casa" cambiado.

    Escenario: El arrendador edita el precio de una propiedad y lo deja vacío
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y escribe su correo "viky.aguilera@gmail.com" y su contraseña "viky1234"
    Y presiona el botón de Log in
    Y presiona el botón de mis propiedades
    Y da clic en el botón de Editar 
    Y actualiza el precio " "
    Y actualiza el tipo de propiedad a "1"
    Y selecciona otra imagen de la propiedad "imagenes_pruebas\Departamento_03.jpg"
    Cuando presiona en el botón Guardar cambios
    Entonces puede ver el mensaje siguiente "Completa este campo" en el campo del precio.