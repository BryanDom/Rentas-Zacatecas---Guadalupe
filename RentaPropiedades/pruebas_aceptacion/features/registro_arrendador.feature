Característica: Registro de arrendador
    Como arrendador del sistema de rentas
    quiero crear mi perfil
    para tener acceso a la plataforma y gestionar mis propiedades.

    Escenario: El arrendador crea su perfil exitosamente
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y presiona el botón Crear cuenta arrendador
    Y escribe su nombre "Luis", sus apellidos "López Pérez", su edad "40"
    Y selecciona su sexo "M"
    Y selecciona su foto de perfil "imagenes_pruebas\arrendador.jpg"
    Y escribe su ocupación "Abogado"
    Y escribe su teléfono "1234567890"
    Y escribe su WhatsApp "1234567890"
    Y escribe su correo "luisperez@gmail.com"
    Y escribe sus preferencias de arrendatarios "Muchachos responsables"
    Y presiona el botón Siguiente
    Y puede ver el mensaje del compromiso del sistema
    Y presiona el botón Aceptar y continuar
    Y ingresa la contraseña "1234"
    Y para confirmar nuevamente ingresa la contraseña "1234"
    Cuando presiona el botón Continuar
    Entonces puede ver el mensaje "¡Cuenta creada exitosamente!"


    Escenario: La dirección de correo electrónico ya está en uso por otro usuario 
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y presiona el botón Crear cuenta arrendador
    Y escribe su nombre "Luis", sus apellidos "López Pérez", su edad "40"
    Y selecciona su sexo "M"
    Y selecciona su foto de perfil "imagenes_pruebas\estudiante.jpg"
    Y escribe su ocupación "Abogado"
    Y escribe su teléfono "1234567890"
    Y escribe su WhatsApp "1234567890"
    Y escribe su correo "acv@gmail.com" 
    Y escribe sus preferencias de arrendatarios "Muchachos responsables"   
    Cuando presiona el botón Siguiente
    Entonces ve un mensaje de error "Ya existe un usuario con ese correo electrónico."

    
    Escenario: Dirección de correo con mal formato
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y presiona el botón Crear cuenta arrendador
    Y escribe su nombre "Luis", sus apellidos "López Pérez", su edad "40"
    Y selecciona su sexo "M"
    Y selecciona su foto de perfil "imagenes_pruebas\estudiante.jpg"
    Y escribe su ocupación "Abogado"
    Y escribe su teléfono "1234567890"
    Y escribe su WhatsApp "1234567890"
    Y escribe su correo "notamail" 
    Y escribe sus preferencias de arrendatarios "Muchachos responsables"   
    Cuando presiona el botón Siguiente
    Entonces ve la alerta "Please include an '@' in the email address. 'notamail' is missing an '@'."

    Escenario: Dato obligatorio no introducido
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y presiona el botón Crear cuenta arrendador
    Y escribe su nombre "Luis", sus apellidos "López Pérez", su edad "40"
    Y selecciona su sexo "M"
    Y selecciona su foto de perfil "imagenes_pruebas\estudiante.jpg"
    Y escribe su ocupación "Abogado"
    Y no escribe su teléfono
    Y escribe su WhatsApp "1234567890"
    Y escribe su correo "notamail" 
    Y escribe sus preferencias de arrendatarios "Muchachos responsables"   
    Cuando presiona el botón Siguiente
    Entonces ve la alerta de error "Please fill out this field."