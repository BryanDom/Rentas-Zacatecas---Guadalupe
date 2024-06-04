Característica: Visualizar reseñas
Como Usuario
Quiero ver las reseñas de las propiedades
Para poder tomar desiciones informadas

Escenario: El usuario estudiante visualizara una propiedad sin reseñas
Dado que el estudiante ingresa a la url "http://localhost:8000/"
Y escribe su correo "elliotnoriega@gmail.com" y su contraseña "elliot@21"
Y presiona el botón de Log in
Y presiona el botón de lista de propiedades
Y presiona el boton detalles de la propiedad "Loma Bonita 23, Lomas de Bernárdez Sección Plata, Guadalupe"
Cuando presiona el boton Reseñas de la propiedad
Entonces ve el titulo "No hay reseñas para esta propiedad"

Escenario: El usuario estudiante visualizara una propiedad con reseñas
Dado que el estudiante ingresa a la url "http://localhost:8000/"
Y escribe su correo "elliotnoriega@gmail.com" y su contraseña "elliot@21"
Y presiona el botón de Log in
Y presiona el botón de lista de propiedades
Y presiona el boton detalles de la propiedad "Villa bonita 2, Colinas Del Padre, Zacatecas"
Cuando presiona el boton Reseñas de la propiedad
Entonces ve el titulo "Lista de reseñas"

Escenario: El usuario arrendador visualizara su propiedad sin reseñas
Dado que el arrendador ingresa a la url "http://localhost:8000/"
Y escribe su correo "elliotnoriega@hotmail.com" y su contraseña "elliot@21"
Y presiona el botón de Log in
Y presiona el botón de mis propiedades
Y presiona el boton detalles de mi propiedad "Loma Bonita 23, Lomas de Bernárdez Sección Plata, Guadalupe"
Cuando presiona el boton Reseñas de la propiedad
Entonces ve el titulo "No hay reseñas para esta propiedad"

Escenario: El usuario arrendador visualizara su propiedad con reseñas
Dado que el arrendador ingresa a la url "http://localhost:8000/"
Y escribe su correo "elliotnoriega@hotmail.com" y su contraseña "elliot@21"
Y presiona el botón de Log in
Y presiona el botón de mis propiedades
Y presiona el boton detalles de mi propiedad "Villa bonita 2, Colinas Del Padre, Zacatecas"
Cuando presiona el boton Reseñas de la propiedad
Entonces ve el titulo "Lista de reseñas"
