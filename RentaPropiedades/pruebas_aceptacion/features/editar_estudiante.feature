Característica: Modificar de estudiante
    Como estudiante del sistema de rentas
    quiero editar mi perfil
    para mantener mi información actualizada.

    Escenario: El estudiante edita su perfil exitosamente
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "estudiante@ejemplo.com" y su contraseña "1234"
    Y presiona el botón de Log in
    Y presiona el botón de ver Perfil
    Y luego click en el botón editar perfil
    Y escribe su nombre "EstudianteNuevo", sus apellidos "EstudianteNuevo", su edad "25"
    Y escribe su universidad actual "Universidad Ejemplo"
    Y escribe su teléfono "0987654321"
    Y escribe su correo "estudiante@ejemplo.com"
    Y escribe sus preferencias de búsqueda "Preferencias nuevas"
    Y escribe sus pasatiempos "Pasatiempos nuevos"
    Cuando presiona el botón Guardar cambios
    Entonces puede ver su nombre "EstudianteNuevo EstudianteNuevo" cambiado.

    

    Escenario: El estudiante no ingresa algún dato obligatorio  
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "estudiante@ejemplo.com" y su contraseña "1234"
    Y presiona el botón de Log in
    Y presiona el botón de ver Perfil
    Y luego click en el botón editar perfil
    Y escribe su nombre "EstudianteNuevo2", sus apellidos "Estudiante Nuevo 2", su edad "24"
    Y selecciona su sexo "F"
    Y escribe su universidad actual " "
    Y escribe su teléfono "4945132552"
    Y escribe su WhatsApp "4945132552"
    Y escribe su correo "estudiante@ejemplo.com"
    Y escribe sus preferencias de búsqueda "Preferencias de prueba"
    Y escribe sus pasatiempos "Pasatiempos nuevos"  
    Cuando presiona el botón Guardar cambios
    Entonces ve un mensaje de error "Este campo es obligatorio."

    Escenario: El estudiante ingresa una dirección de correo electrónico no válida
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "estudiante@ejemplo.com" y su contraseña "1234"
    Y presiona el botón de Log in
    Y presiona el botón de ver Perfil
    Y luego click en el botón editar perfil
    Y escribe su nombre "EstudianteNuevo2", sus apellidos "Estudiante Nuevo 2", su edad "24"
    Y selecciona su sexo "F"
    Y escribe su universidad actual "Uaz Nueva"
    Y escribe su teléfono "4945132552"
    Y escribe su WhatsApp "4945132552"
    Y escribe su correo "nuevocorreo@"
    Y escribe sus preferencias de búsqueda "Preferencias de prueba"
    Y escribe sus pasatiempos "Pasatiempos nuevos"    
    Cuando presiona el botón Guardar cambios
    Entonces ve un mensaje de error en el correo "Ingresa texto después del signo '@'. La dirección 'nuevocorreo@' está incompleta."


    Escenario: La dirección de correo electrónico ya está en uso por otro usuario
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "estudiante@ejemplo.com" y su contraseña "1234"
    Y presiona el botón de Log in
    Y presiona el botón de ver Perfil
    Y luego click en el botón editar perfil
    Y escribe su nombre "EstudianteNuevo2", sus apellidos "Estudiante Nuevo 2", su edad "24"
    Y selecciona su sexo "F"
    Y escribe su universidad actual "Uaz Nueva"
    Y escribe su teléfono "4945132552"
    Y escribe su WhatsApp "4945132552"
    Y escribe su correo "brayandominguezs20@gmail.com"
    Y escribe sus preferencias de búsqueda "Preferencias de prueba"
    Y escribe sus pasatiempos "Pasatiempos nuevos"    
    Cuando presiona el botón Guardar cambios
    Entonces ve un mensaje de error "Ya existe un usuario con ese correo electrónico y tiene una contraseña asociada."