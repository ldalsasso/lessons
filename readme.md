# Sistema de Lecciones de Amigos

- Este sistema es una API que permite conocer los cursos realizados por los amigos de un usuario.



## Requerimientos principales:

- Python 3.8.10
- Django==3.1.5
- djangorestframework 3.13.1
- djangorestframework-timed-auth-token 1.3.0



## Instalación y uso:

Para poder correr el proyecto es necesario seguir los siguientes pasos:

- Crear un entorno virtual donde alojar el proyecto
- Clonar el repositorio.
- Pararse en la rama "master".
- Crear la base de datos "julasoft_db".
- Migrar la base de datos: python manage.py migrate
- Crear un usuario superuser. Para crearlo usar la instrucción: python manage.py createsuperuser
- Correr el servior local mediante: python manage.py runserver
- Importar la colección de postman que se encuentra en la carpeta "postman" para poder correr los endpoints.
- Obtener token del superuser mediante el request que se encuentra en Postman en Authentication/Account Token SuperAdmin. Previamente cambiar los datos de usuario y password por los del usuario recientemente creado.
- En la carpeta "User" de Postman se encuentran todos los requests necesarios para el llamado a los endpoints correspondientes a User.
- En la carpeta "Courses" de Postman se encuentran todos los requests necesarios para el llamado a los endpoints correspondientes a Cursos.
- En la carpeta "Lessons" de Postman se encuentran todos los requests necesarios para el llamado a los endpoints correspondientes a Lecciones.
- En la carpeta "Friends" de Postman se encuentran todos los requests necesarios para el llamado a los endpoints correspondientes a Amigos.



## Endpoints:

Todos los endpoint para la gestión de Cursos, Lecciones y Amigos requiere autenticación.

- Crear un usuario no superadmin - Create User - POST - /api/v1/users/
- Modificar un usuario - Update User - PUT - /api/v1/users/[id]/
- Modificar parcialmente un usuario - Partial Update User - PATCH - /api/v1/users/[id]/
- Eliminar un usuario - Delete - DELETE - /api/v1/users/[id]/
- Listar todos los usuarios - GetAll - GET - /api/v1/users/
- Consultar un usuarios - Get by Id - GET - /api/v1/users/[id]/
- Crear Token - Account Token - POST - /api/v1/user/auth/login/
- Crear un nuevo curso - POST - /api/v1/courses/
- Modificar un curso existente - PUT - /api/v1/lessons/[id]
- Borrar un curso existente - DELETE - /api/v1/courses/[id]
- Listar todos los cursos existente - GET - /api/v1/courses/
- Listar un curso mediante id - GET - /api/v1/courses/[id]
- Crear un nueva lección - POST - /api/v1/lessons/
- Listar todos los cursos existente (Login: Superuser) - GET - /api/v1/lessons/
- Listar todos los cursos existente por usuario (Login: User) - GET - /api/v1/lessons/
- Crear un amigo - POST - /api/v1/friends/
- Listar todos los amigos (Login: Superuser) - GET - /api/v1/friends/
- Listar todos los amigos de un usuario (Login: User) - GET - /api/v1/friends/



## Test:

Para poder correr los test ejecutar la siguiente instrucción:

- pytest tests/ --create-db
