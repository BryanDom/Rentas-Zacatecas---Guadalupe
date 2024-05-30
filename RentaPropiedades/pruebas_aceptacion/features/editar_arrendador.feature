Característica: Modificar arrendador
    Como arrendador del sistema de rentas
    quiero editar mi perfil
    para mantener mi información actualizada.

    Escenario: El arrendador edita su perfil exitosamente
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y escribe su correo "luisperez@gmail.com" y su contraseña "1234"
    Y presiona el botón de Log in
    Y presiona el botón de ver Perfil arrendador
    Y luego click en el botón editar perfil arrendador
    Y escribe su nombre "Dr.Luis", sus apellidos "Pérez López", su edad "41"
    Y escribe su ocupación "Abogado"
    Y escribe su teléfono "1234567890"
    Y escribe su WhatsApp "1234567890"
    Y escribe su correo "luisperez@gmail.com"
    Y escribe sus preferencias de arrendatarios "Muchachos responsables"
    Cuando da click en el botón Guardar cambios 
    Entonces puede ver su nombre "Dr.Luis Pérez López" cambiado.