# Protocolo de comunicaciones entre servicios
En este documento vamos a describir los endpoints de los APIs REST, el diseño de tablas de datos del backend y como se comunican entre sí. 



**Tabla de contenidos**
 1. [Endpoints](https://github.com/Alvaro9rc/practica-dms-2021-2022/edit/main/Memoria/ProtocoloComunicaciones.md "Endpoints")
 2. [Tablas de la base de datos](https://github.com/Alvaro9rc/practica-dms-2021-2022/edit/main/Memoria/ProtocoloComunicaciones.md "Tablas de la base de datos")
 3. [Comunicación](https://github.com/Alvaro9rc/practica-dms-2021-2022/edit/main/Memoria/ProtocoloComunicaciones.md "Comunicación")



Endpoints 
-------------

### /questions:

-GET

-Descripción: Consigue la lista de preguntas 

-Responses: 

          - 200: Correcto

-Comunicación: Este endpoint se comunica con la clase `dms2122backend.presentation.rest.question` y accede al método `def list_questions()`

### /question/new:

-POST

-Descripción: Crea una nueva pregunta

-Responses: 

            - 200: Correcto 
            - 400: Fallo en la petición            
            - 403: Fallo debido a falta de permisos del usuario       
            - 409: Fallo en la pregunta
            
-Comunicación: Este endpoint se comunica con la clase `dms2122backend.presentation.rest.question` y accede al método `def create_question()`

### /question/{id}/answer/{username}:

-POST

-Descripción: Respuesta de una pregunta

-Responses:

            - 200: Correcto
            - 400: Error en la petición
            - 403: El usuario no tiene los permisos necesarios
            - 404: La pregunta no existe
            
-Comunicación: Este endpoint se comunica con la clase `dms2122backend.presentation.rest.answer` y accede al método `def create_question_answer()`


### answers/{id}:

-GET

-Descripción: Devuelve todas las respuesta de una pregunta

-Responses:

            - 200: Correcto
            - 400: Fallo porque un parametro no se ha pasado
            - 403: El usuario no tiene los permisos necesarios
            
-Comunicación: Este endpoint se comunica con la clase `dms2122backend.presentation.rest.answer` y accede al método `def list_all_for_user()`


Tablas de la base de datos 
-------------

### question

Columna  | Tipo         |   PK    | Nullabe
--------- | ----------  | ------- | --------
id        | Integer |TRUE  | FALSE
questionName | String(64) |    FALSE    | FALSE
description   | String(64) |    FALSE    | FALSE
questionAnswer | String(64) |  FALSE     | FALSE
questionAnswer2 | String(64) | FALSE     |  FALSE
questionAnswer3  | String(64) | FALSE    | FALSE
correctAnswer    | Integer | FALSE       | FALSE
puntuation       | Float(2,2) |  FALSE   | FALSE
penalty          | Float(2,2) |  FALSE     | FALSE


### answer

Columna  | Tipo        
--------- | ----------  
id        | Integer 
answer | String(64) 
valoration   | Integer 
username | String(64) 


Comunicación 
-------------

La comunicación por parte del backend con el componente auth se realiza en la clase `dms2122backend/data/config/backendconfiguration.py`. En esta clase es donde se inicializa la conexión con la base de datos temporal, los tokens de usuarios y los servicios de auth. Estos tokens de usuario son verificados por la clase `security.py` para ver si estan correctos, si son autorizados... 

La clase `schema.py` es la responsabe de la gestión de la conexión con la base de datos. 
