Característica: Registro de propiedad
    Como arrendador
    quiero crear una nueva propiedad
    para publicar la propiedad y atraer inquilinos potenciales.

    Escenario: El arrendador registra una nueva propiedad exitosamente
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y escribe su correo "viky.aguilera@gmail.com" y su contraseña "viky1234"
    Y presiona el botón de Log in
    Y presiona el botón de mis propiedades
    Y da clic en Nueva Propiedad
    Y escribe la descripción de la propiedad "Departamento con 2 habitaciones, baño, cocina y sala"
    Y escribe el precio "4300"
    Y selecciona el tipo de propiedad "2"
    Y escribe la calle "Calle González Ortega"
    Y escribe el número "125"
    Y selecciona el municipio "Zacatecas"
    Y selecciona la colonia "Zacatecas Centro"
    Y selecciona la primera imagen de la propiedad "imagenes_pruebas\Departamento_01.jpg"
    Y selecciona la segunda imagen de la propiedad "imagenes_pruebas\Departamento_02.jpg"
    Y palomea la opción de servicios incluidos
    Y después palomea la opción de info verídica
    Cuando presiona el botón Agregar
    Entonces puede ver el siguiente mensaje "¡Propiedad agregada con éxito!"

    Escenario: El arrendador registra una propiedad existente
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y escribe su correo "viky.aguilera@gmail.com" y su contraseña "viky1234"
    Y presiona el botón de Log in
    Y presiona el botón de mis propiedades
    Y da clic en Nueva Propiedad
    Y escribe la descripción de la propiedad "Departamento con 2 habitaciones, baño, cocina y sala"
    Y escribe el precio "4300"
    Y selecciona el tipo de propiedad "2"
    Y escribe la calle "Calle González Ortega"
    Y escribe el número "125"
    Y selecciona el municipio "Zacatecas"
    Y selecciona la colonia "Zacatecas Centro"
    Y selecciona la primera imagen de la propiedad "imagenes_pruebas\Departamento_01.jpg"
    Y selecciona la segunda imagen de la propiedad "imagenes_pruebas\Departamento_02.jpg"
    Y palomea la opción de servicios incluidos
    Y después palomea la opción de info verídica
    Cuando presiona el botón Agregar
    Entonces puede ver el siguiente mensaje de error "Error: La propiedad ya está registrada."

    Escenario: El arrendador registra una propiedad con precio de 0 pesos
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y escribe su correo "viky.aguilera@gmail.com" y su contraseña "viky1234"
    Y presiona el botón de Log in
    Y presiona el botón de mis propiedades
    Y da clic en Nueva Propiedad
    Y escribe la descripción de la propiedad "Departamento con 2 habitaciones, baño, cocina y sala"
    Y escribe el precio "0"
    Y selecciona el tipo de propiedad "2"
    Y escribe la calle "Calle González Ortega"
    Y escribe el número "125"
    Y selecciona el municipio "Zacatecas"
    Y selecciona la colonia "Zacatecas Centro"
    Y selecciona la primera imagen de la propiedad "imagenes_pruebas\Departamento_01.jpg"
    Y selecciona la segunda imagen de la propiedad "imagenes_pruebas\Departamento_02.jpg"
    Y palomea la opción de servicios incluidos
    Y después palomea la opción de info verídica
    Cuando presiona el botón Agregar
    Entonces puede ver el mensaje de error "El valor debe ser superior o igual a 100"

    Escenario: El arrendador registra una propiedad sin descripción
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y escribe su correo "viky.aguilera@gmail.com" y su contraseña "viky1234"
    Y presiona el botón de Log in
    Y presiona el botón de mis propiedades
    Y da clic en Nueva Propiedad
    Y escribe el precio "1000"
    Y selecciona el tipo de propiedad "2"
    Y escribe la calle "Calle González Ortega"
    Y escribe el número "125"
    Y selecciona el municipio "Zacatecas"
    Y selecciona la colonia "Zacatecas Centro"
    Y selecciona la primera imagen de la propiedad "imagenes_pruebas\Departamento_01.jpg"
    Y selecciona la segunda imagen de la propiedad "imagenes_pruebas\Departamento_02.jpg"
    Y palomea la opción de servicios incluidos
    Y después palomea la opción de info verídica
    Cuando presiona el botón Agregar
    Entonces ve el mensaje en el campo descripcion "Completa este campo"

    Escenario: El arrendador registra una propiedad sin imágenes (obligatorias)
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y escribe su correo "viky.aguilera@gmail.com" y su contraseña "viky1234"
    Y presiona el botón de Log in
    Y presiona el botón de mis propiedades
    Y da clic en Nueva Propiedad
    Y escribe la descripción de la propiedad "Departamento con 2 habitaciones, baño, cocina y sala"
    Y escribe el precio "1000"
    Y selecciona el tipo de propiedad "2"
    Y escribe la calle "Calle González Ortega"
    Y escribe el número "125"
    Y selecciona el municipio "Zacatecas"
    Y selecciona la colonia "Zacatecas Centro"
    Y palomea la opción de servicios incluidos
    Y después palomea la opción de info verídica
    Cuando presiona el botón Agregar
    Entonces puede ver la siguiente alerta "Selecciona un archivo"

    Escenario: El arrendador registra una propiedad sin servicios incluidos
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y escribe su correo "viky.aguilera@gmail.com" y su contraseña "viky1234"
    Y presiona el botón de Log in
    Y presiona el botón de mis propiedades
    Y da clic en Nueva Propiedad
    Y escribe la descripción de la propiedad "Casa de 3 habitaciones, sala-comedor, cocina, 1 baño"
    Y escribe el precio "1000"
    Y selecciona el tipo de propiedad "2"
    Y escribe la calle "Calle Buenavista"
    Y escribe el número "125"
    Y selecciona el municipio "Zacatecas"
    Y selecciona la colonia "Buenavista"
    Y selecciona la primera imagen de la propiedad "imagenes_pruebas\Departamento_01.jpg"
    Y selecciona la segunda imagen de la propiedad "imagenes_pruebas\Departamento_02.jpg"
    Y después palomea la opción de info verídica
    Cuando presiona el botón Agregar
    Entonces puede ver el siguiente mensaje "¡Propiedad agregada con éxito!"

    Escenario: El arrendador registra una propiedad sin aceptar que es info verídica
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y escribe su correo "viky.aguilera@gmail.com" y su contraseña "viky1234"
    Y presiona el botón de Log in
    Y presiona el botón de mis propiedades
    Y da clic en Nueva Propiedad
    Y escribe la descripción de la propiedad "Casa de 3 habitaciones, sala-comedor, cocina, 1 baño"
    Y escribe el precio "1000"
    Y selecciona el tipo de propiedad "2"
    Y escribe la calle "Calle Buenavista"
    Y escribe el número "125"
    Y selecciona el municipio "Zacatecas"
    Y selecciona la colonia "Buenavista"
    Y selecciona la primera imagen de la propiedad "imagenes_pruebas\Departamento_01.jpg"
    Y selecciona la segunda imagen de la propiedad "imagenes_pruebas\Departamento_02.jpg"
    Cuando presiona el botón Agregar
    Entonces puede ver la siguiente alerta de seguridad "Selecciona esta casilla de verificación si quieres continuar"

    Escenario: El arrendador registra una nueva propiedad sin especificar el municipio 
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y escribe su correo "viky.aguilera@gmail.com" y su contraseña "viky1234"
    Y presiona el botón de Log in
    Y presiona el botón de mis propiedades
    Y da clic en Nueva Propiedad
    Y escribe la descripción de la propiedad "Casa con 2 habitaciones, baño, cocina y sala"
    Y escribe el precio "4300"
    Y selecciona el tipo de propiedad "2"
    Y escribe la calle "Calle Hidalgo"
    Y escribe el número "58"
    Y selecciona la primera imagen de la propiedad "imagenes_pruebas\Departamento_01.jpg"
    Y selecciona la segunda imagen de la propiedad "imagenes_pruebas\Departamento_02.jpg"
    Y palomea la opción de servicios incluidos
    Y después palomea la opción de info verídica
    Cuando presiona el botón Agregar
    Entonces ve el mensaje "Selecciona un elemento de la lista"