# real_state_project
Proyecto inmobiliario para la consulta de inmuebles, interacciones sociales con las publicaciones y consultas

### OBJETIVO ###

Herramienta en la que los usuarios puedan consultar los inmuebles disponibles para la venta. En esta herramienta los usuarios podrán ver el estatus en que se encuentran los inmuebles, junto con una descripcion detallada del mismo, con el objetivo de facilitar la búsqueda, a través de filtros de búsqueda.

Adicionalmente, los usuarios podrán darle “me gusta” a los inmuebles con el fin de tener un ranking interno de los inmuebles más llamativos.


### TECNOLOGÍAS A UTILIZAR ###

Arquitectura: Modular
Lenguaje: Python v. 13.3.63
Base de datatos: Mysql

### Endpoints disponibles (resumen)

- Properties
  - GET /properties (listado con estado actual desde `status_history`)
  - GET /properties/{id}
  - POST /properties
  - PATCH /properties/{id}
  - DELETE /properties/{id}

  image.png
  

- Likes
  - POST /likes (toggle: crea o elimina like si ya existe)
  - DELETE /likes/{id}

- Auth
  - POST /signup (crea usuario en `auth_user`)
  - POST /login (JWT)
  - POST /logout

### Notas de modelado con la BD existente
- Usuarios: se utiliza `auth_user` para autenticación. `users` se mantiene como módulo opcional para perfil extendido.
- Inmuebles: tabla `property`. El estado visible se calcula como el último registro de `status_history` por `property_id`, unido a `status.name`.

### Mejoras opcionales (plan a futuro)
- Property
  - `image_url` (URL de imagen principal)
  - `property_type`, `property_subtype` (ej. apartamento/loft, casa/campestre)
  - `property_size` (área)
  - `status_id` cacheado en `property` para acelerar listados (manteniendo `status_history` como fuente de verdad)
  - `url` pública del inmueble
  - `neighborhood`/barrio
  - índices por (`city`, `year`) y por (`status_id`, `update_date`)

- Users (perfil extendido)
  - `phone`, `city` y otros datos de contacto (separado de `auth_user`)
  - Avatar/`image_url`

- Likes
  - Conteo por inmueble (`/properties/{id}/likes/count`)
  - Historial de likes por usuario (`/likes?user_id=`)

- Auth
  - Refrescar tokens JWT (refresh_token + access_token)
  - Blacklist/whitelist para logout con estado

- General
  - Paginación, filtros por `status` visible (pre_venta|en_venta|vendido), `city`, `year_from/year_to`
  - Logs estructurados, trazabilidad por request-id
  - Tests unitarios de repos y servicios
