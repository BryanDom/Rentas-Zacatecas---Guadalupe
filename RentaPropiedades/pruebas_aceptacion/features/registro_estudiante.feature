Característica: Registro de estudiante
    Como estudiante del sistema de rentas
    quiero crear mi perfil
    para tener acceso a la plataforma y gestionar mis preferencias.

    Escenario: El estudiante crea su perfil exitosamente
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y presiona el botón Crear cuenta estudiante
    Y escribe su nombre "Estudiante1", sus apellidos "Estudiante Estudiante", su edad "24"
    Y selecciona su sexo "M"
    Y selecciona su foto de perfil "C:/Users/brayan/Downloads/estudiante.png"
    Y escribe su universidad actual "Universidad Ejemplo"
    Y escribe su teléfono "1234567890"
    Y escribe su WhatsApp "1234567890"
    Y escribe su correo "estudiante@ejemplo.com"
    Y escribe sus preferencias de búsqueda "Preferencias de prueba"
    Y escribe sus pasatiempos "Pasatiempos de prueba"
    Y presiona el botón Siguiente
    Y puede ver el mensaje del compromiso del sistema
    Y presiona el botón Aceptar y continuar
    Y ingresa la contraseña "1234"
    Y para confirmar nuevamente ingresa la contraseña "1234"
    Cuando presiona el botón Continuar
    Entonces puede ver el mensaje "¡Cuenta creada exitosamente!"


    Escenario: El estudiante no ingresa algún dato obligatorio  
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y presiona el botón Crear cuenta estudiante
    Y escribe su nombre "Estudiante1", sus apellidos "Estudiante Estudiante", su edad "24"
    Y selecciona su sexo "M"
    Y selecciona su foto de perfil "C:/Users/brayan/Downloads/estudiante.png"
    Y escribe su universidad actual "Universidad Ejemplo"
    Y escribe su teléfono "1234567890"
    Y escribe su WhatsApp "1234567890"
    Y escribe su correo "estudiante@ejemplo.com"
    Y escribe sus preferencias de búsqueda "Preferencias de prueba"
    Y no completa el campo de pasatiempos " "   
    Cuando presiona el botón Siguiente
    Entonces ve un mensaje de error "Este campo es obligatorio."

    Escenario: El estudiante ingresa una dirección de correo electrónico no válida
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y presiona el botón Crear cuenta estudiante
    Y escribe su nombre "Estudiante1", sus apellidos "Estudiante Estudiante", su edad "24"
    Y selecciona su sexo "M"
    Y selecciona su foto de perfil "C:/Users/brayan/Downloads/estudiante.png"
    Y escribe su universidad actual "Universidad Ejemplo"
    Y escribe su teléfono "1234567890"
    Y escribe su WhatsApp "1234567890"
    Y escribe su correo "estudiante@"
    Y escribe sus preferencias de búsqueda "Preferencias de prueba"
    Y escribe sus pasatiempos "Pasatiempos de prueba"  
    Cuando presiona el botón Siguiente
    Entonces ve un mensaje de error en el correo "Ingresa texto después del signo '@'. La dirección 'estudiante@' está incompleta."


    Escenario: La dirección de correo electrónico ya está en uso por otro usuario 
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y presiona el botón Crear cuenta estudiante
    Y escribe su nombre "Estudiante1", sus apellidos "Estudiante Estudiante", su edad "24"
    Y selecciona su sexo "M"
    Y selecciona su foto de perfil "C:/Users/brayan/Downloads/estudiante.png"
    Y escribe su universidad actual "Universidad Ejemplo"
    Y escribe su teléfono "1234567890"
    Y escribe su WhatsApp "1234567890"
    Y escribe su correo "estudiante@ejemplo.com"
    Y escribe sus preferencias de búsqueda "Preferencias de prueba"
    Y escribe sus pasatiempos "Pasatiempos de prueba"  
    Cuando presiona el botón Siguiente
    Entonces ve un mensaje de error "Ya existe un usuario con ese correo electrónico."