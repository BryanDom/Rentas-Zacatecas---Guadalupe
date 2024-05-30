Característica: Aplicar filtros de búsqueda
    Como estudiante del sistema de rentas
    quiero utilizar filtros de búsqueda
    para ver solo las propiedades que se adapten a lo que necesito

    Escenario: El estudiante filtra por precios
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "acv@gmail.com" y su contraseña "adal1234" 
    Y presiona el botón de Log in
    Y presiona el botón lista de propiedades
    Y selecciona un precio minimo "1000"
    Y selecciona un precio maximo "2000"
    Y da click en aplicar filtros
    Entonces puede ver una lista de resultados


    Escenario: El estudiante filtra por ubicación
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "acv@gmail.com" y su contraseña "adal1234" 
    Y presiona el botón de Log in
    Y presiona el botón lista de propiedades
    Y selecciona un Municipio "Zacatecas"
    Y selecciona una colonia "Colinas del padre"
    Y da click en aplicar filtros
    Entonces puede ver una lista de resultados

    Escenario: El estudiante filtra por tipo de propiedad
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "acv@gmail.com" y su contraseña "adal1234" 
    Y presiona el botón de Log in
    Y presiona el botón lista de propiedades
    Y selecciona un Tipo de propiedad "Departamento"
    Y da click en aplicar filtros
    Entonces puede ver una lista de resultados


