# real_state_project
Proyecto inmobiliario para la consulta de inmuebles, interacciones sociales con las publicaciones y consultas

### OBJETIVO ###

Herramienta en la que los usuarios puedan consultar los inmuebles disponibles para la venta. En esta herramienta los usuarios podrán ver el estatus en que se encuentran los inmuebles, junto con una descripcion detallada del mismo, con el objetivo de facilitar la búsqueda, a través de filtros de búsqueda.

Adicionalmente, los usuarios podrán darle “me gusta” a los inmuebles con el fin de tener un ranking interno de los inmuebles más llamativos.


### TECNOLOGÍAS A UTILIZAR ###

Arquitectura: Modular
Lenguaje: Python v. 13.3.63
Base de datatos: Mysql

### Endpoints disponibles ###

C --> POST /inmuebles
R --> GET /inmuebles
U --> UPDATE /inmuebles
D --> DELETE /inmuebles

Body {
    status:
    city:
    address:
    description:
    price:
}

C --> POST /user
R --> GET /user
U --> UPDATE /user
D --> DELETE /user

Body {
    nombre:
    correo:
    password:
    ciudad:
    telefono:
}
