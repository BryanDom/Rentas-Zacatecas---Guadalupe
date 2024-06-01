Característica: Iniciar sesión
    Como Usuario
    Quiero iniciar sesión en mi cuenta
    Para poder acceder a las funcionalidades de la plataforma


    Escenario: El usuario inicia sesión de forma exitosa
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "elliotnoriega@gmail.com" y su contraseña "elliot@21" 
    Cuando presiona el botón de Log in
    Entonces ve el titulo "Bienvenido estudiante"

    Escenario: El usuario ingresa una contraseña invalida 
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "elliotnoriega@gmail.com" y su contraseña "elliot@" 
    Cuando presiona el botón de Log in
    Entonces ve la alerta: "Contraseña incorrecta :("

    Escenario: El usuario ingresa una correo no registrado 
    Dado que el estudiante ingresa a la url "http://localhost:8000/"
    Y escribe su correo "elliot@gmail.com" y su contraseña "elliot@21" 
    Cuando presiona el botón de Log in
    Entonces ve la alerta: "Aún no te has registrado. Inicia tu registro :)."

    Escenario: El usuario inicia sesión de forma exitosa
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y escribe su correo "elliotnoriega@hotmail.com" y su contraseña "elliot@21" 
    Cuando presiona el botón de Log in
    Entonces ve el titulo "Bienvenido arrendador"

    Escenario: El usuario ingresa una contraseña invalida 
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y escribe su correo "elliotnoriega@hotmail.com" y su contraseña "elliot@" 
    Cuando presiona el botón de Log in
    Entonces ve la alerta: "Contraseña incorrecta :("

    Escenario: El usuario ingresa una correo no registrado 
    Dado que el arrendador ingresa a la url "http://localhost:8000/"
    Y escribe su correo "elliot@hotmail.com" y su contraseña "elliot@21" 
    Cuando presiona el botón de Log in
    Entonces ve la alerta: "Aún no te has registrado. Inicia tu registro :)."