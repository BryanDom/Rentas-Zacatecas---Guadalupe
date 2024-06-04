Característica: Registro de estudiante
Como estudiante del sistema de rentas
quiero crear mi perfil
para tener acceso a la plataforma y gestionar mis preferencias.

Escenario: El estudiante crea su perfil exitosamente
Dado que el estudiante ingresa a la url "http://localhost:8000/"
Y presiona el botón Crear cuenta estudiante
Y escribe su nombre "Estudiante1", sus apellidos "Estudiante Estudiante", su edad "24"
Y selecciona su sexo "M"
Y selecciona su foto de perfil "imagenes_pruebas\estudiante.jpg"
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

Escenario: La dirección de correo electrónico ya está en uso por otro usuario
Dado que el estudiante ingresa a la url "http://localhost:8000/"
Y presiona el botón Crear cuenta estudiante
Y escribe su nombre "Estudiante1", sus apellidos "Estudiante Estudiante", su edad "24"
Y selecciona su sexo "M"
Y selecciona su foto de perfil "imagenes_pruebas\estudiante.jpg"
Y escribe su universidad actual "Universidad Ejemplo"
Y escribe su teléfono "1234567890"
Y escribe su WhatsApp "1234567890"
Y escribe su correo "estudiante@ejemplo.com"
Y escribe sus preferencias de búsqueda "Preferencias de prueba"
Y escribe sus pasatiempos "Pasatiempos de prueba"
Cuando presiona el botón Siguiente
Entonces ve un mensaje de error "Ya existe un usuario con ese correo electrónico."

Escenario: Dirección de correo con mal formato
Dado que el estudiante ingresa a la url "http://localhost:8000/"
Y presiona el botón Crear cuenta estudiante
Y escribe su nombre "Estudiante1", sus apellidos "Estudiante Estudiante", su edad "24"
Y selecciona su sexo "M"
Y selecciona su foto de perfil "imagenes_pruebas\estudiante.jpg"
Y escribe su universidad actual "Universidad Ejemplo"
Y escribe su teléfono "1234567890"
Y escribe su WhatsApp "1234567890"
Y escribe su correo "notamail"
Y escribe sus preferencias de búsqueda "Preferencias de prueba"
Y escribe sus pasatiempos "Pasatiempos de prueba"
Y presiona el botón Siguiente
Entonces ve la alerta "Please include an '@' in the email address. 'notamail' is missing an '@'."

Escenario: Campo obligatorio no ingresado
Dado que el estudiante ingresa a la url "http://localhost:8000/"
Y presiona el botón Crear cuenta estudiante
Y escribe su nombre "Estudiante1", sus apellidos "Estudiante Estudiante", su edad "24"
Y selecciona su sexo "M"
Y selecciona su foto de perfil "imagenes_pruebas\estudiante.jpg"
Y escribe su universidad actual "Universidad Ejemplo"
Y no escribe su teléfono
Y escribe su WhatsApp "1234567890"
Y escribe su correo "notamail"
Y escribe sus preferencias de búsqueda "Preferencias de prueba"
Y escribe sus pasatiempos "Pasatiempos de prueba"
Y presiona el botón Siguiente
Entonces ve la alerta de error "Please fill out this field."
