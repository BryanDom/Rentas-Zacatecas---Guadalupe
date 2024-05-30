Característica: Visualizar perfil de estudiante
    Como estudiante del sistema de rentas
    quiero ver mi perfil
    para consultar mi información personal.

    Escenario: El estudiante ve su perfil exitosamente
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "estudiante@ejemplo.com" y su contraseña "1234" 
    Y presiona el botón de Log in
    Cuando presiona el botón de ver Perfil
    Entonces puede ver su nombre completo "Estudiante1 Estudiante Estudiante"
    Y puede ver su edad "24"
    Y puede ver su sexo "Masculino"
    Y puede ver su universidad actual "Universidad Ejemplo"
    Y puede ver su teléfono "1234567890"
    Y puede ver sus preferencias de búsqueda "Preferencias de prueba"
    Y puede ver sus pasatiempos "Pasatiempos de prueba"
    Y puede ver los botones para editar perfil y contacto