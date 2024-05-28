Característica: Eliminar perfil de estudiante
    Como estudiante del sistema de rentas
    quiero eliminar mi perfil
    para dejar de usar la plataforma y borrar mis datos personales.

    Escenario: El usuario puede eliminar su perfil de manera exitosamente
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "estudiante@ejemplo.com" y su contraseña "1234" 
    Y presiona el botón de Log in
    Y presiona el botón de ver Perfil
    Y luego click en el botón editar perfil
    Y presiona el botón Eliminar Perfil
    Y puede ver el mensaje "¿Estás seguro de eliminar tu perfil?"
    Cuando presiona el botón Eliminar Perfil
    Entonces puede ver el mensaje "Usuario eliminado con exito".