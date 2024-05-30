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
    Y escribe su WhatsApp "4945132552"
    Y escribe su correo "estudiante@ejemplo.com"
    Y escribe sus preferencias de búsqueda "Preferencias nuevas"
    Y escribe sus pasatiempos "Pasatiempos nuevos"
    Cuando presiona el botón Guardar cambios
    Entonces puede ver su nombre "EstudianteNuevo EstudianteNuevo" cambiado.