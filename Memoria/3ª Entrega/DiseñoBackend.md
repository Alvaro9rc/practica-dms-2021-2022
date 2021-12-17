# Arquitectura y diseño del backend
En este documento vamos a comentar todos los aspectos relacionados con la arquitectura y diseño del backend.


**Tabla de contenidos**
 1. [Arquitectura escogida](https://github.com/Alvaro9rc/practica-dms-2021-2022/edit/main/Memoria/DiseñoBackend.md "Arquitectura escogida")
 2. [Mecanismos de reutilización](https://github.com/Alvaro9rc/practica-dms-2021-2022/edit/main/Memoria/DiseñoBackend.md "Mecanismos de reutilización")
 3. [Patrones de comportamiento](https://github.com/Alvaro9rc/practica-dms-2021-2022/edit/main/Memoria/DiseñoBackend.md "Patrones de comportamiento")


Arquitectura escogida
-------------

Para satisfacer las necesidades que necesita el software se ha elegido un **patrón multicapa**, ya que de esta forma podemos aprovechar las ventajas que nos ofrece este diseño, como minimizar las dependencias y mejorar la encapsulación.

En concreto se ha implementado un **modelo de 3 capas.**

* **Capa de origen de datos**

Esta capa corresponde con `dms2122backend/dms2122backend/data` . En esta carpeta tenemos aparte de la configuración de comunicaciones mencionada en el apartado "Protocolo de comunicaciones" también tenemos los ficheros donde residen las tablas de las bases de datos. Estas tablas son `question` y `answer`. Separamos la creación y definición de las tablas con su gestión para mantener centradas las responsabilidades y que sea un código más legible donde sepas a donde acudir si quieres redefinir tablas o redifinir métodos de gestión de preguntas/respuestas. 


* **Capa de presentación**

Esta capa corresponde con `dms2122backend/dms2122backend/presentation` . Las clases de esta carpeta solo muestra los datos y no gestiona ni modifica nada, solo presenta.
Como siempre separamos las preguntas de las respuestas para mantener centradas las responsabilidades y para que una clase no depende de métodos de algo totalmente diferente. Mismo criterio que en el frontend. 


* **Capa de lógica de dominio**

Esta capa corresponde con `dms2122backend/dms2122backend/service` . Aquí es donde manejamos todo lo relacionado con las preguntas y respuestas. Hemos intentado evitar la arquitectura en 4 capas debido a no aumentar la dificultad para leer y entender el código y para seguir con la misma estructura que la anterior entrega hemos eliminado la carpeta de logica y metido todo lo relacionado con ella en service. Misma intención que siempre, diferenciar en clases diferentes preguntas de respuestas. 


Mecanismos de reutilización
-------------

En esta parte hemos utilizado sobretodo el mecanismo de **Delegación**. Vemos por ejemplo que muchas clases llamamos a `questionservices.py` es decir llamamos a esta clase cuando una clase intermedia recibe la petición. Esta decisión la hemos tomado para intentar no mezclar las capas y que por ejemplo en la capa de datos haya operaciones de preguntas y respuestos y así mantener el principio de Single Responsabilty. 
Nos facilita también mucho la tarea al saber que todo lo que haya que cambiar realcionado con la gestion de preguntas/respuestas está en la carpeta service y asi no volvernos locos buscando en diferentes clases de otras carpetas. 
 
 
Patrones de comportamiento
-------------

Con lo referente al cambio de roles de los usuarios, podemos aplicar el patrón estado, ya que dependiendo del rol, que puede cambiar dinámicamente también, cada usuario tendrá distintas funcionalidades.








