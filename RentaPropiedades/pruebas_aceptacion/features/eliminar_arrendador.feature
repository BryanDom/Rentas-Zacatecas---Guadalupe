Característica: Eliminar perfil de arrendador
    Como arrendador del sistema de rentas
    quiero eliminar mi perfil
    para dejar de usar la plataforma y borrar mis datos personales.

    Escenario: El usuario puede eliminar su perfil exitosamente
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y escribe su correo "luisperez@gmail.com" y su contraseña "1234" 
    Y presiona el botón de Log in
    Y presiona el botón de ver Perfil arrendador
    Y luego click en el botón editar perfil arrendador
    Y presiona el botón Eliminar Perfil arrendador
    Y puede ver el mensaje "¿Estás seguro de eliminar tu perfil?"
    Cuando presiona el botón Eliminar Perfil arrendador
    Entonces puede ver el mensaje "¿No tienes cuenta? Crea una".