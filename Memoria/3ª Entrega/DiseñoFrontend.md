# Arquitectura y diseño del frontend
En este documento vamos a comentar todos los aspectos relacionados con la arquitectura y diseño del frontend.



**Tabla de contenidos**
 1. [Arquitectura escogida](https://github.com/Alvaro9rc/practica-dms-2021-2022/edit/main/Memoria/DiseñoFrontend.md "Arquitectura escogida")
 2. [Mecanismos de reutilización](https://github.com/Alvaro9rc/practica-dms-2021-2022/edit/main/Memoria/DiseñoFrontend.md "Mecanismos de reutilización")
 3. [Decisiones referidas a los principios SOLID](https://github.com/Alvaro9rc/practica-dms-2021-2022/edit/main/Memoria/DiseñoFrontend.md "Decisiones referidas a los principios SOLID")
 4. [Patrón de diseño](https://github.com/Alvaro9rc/practica-dms-2021-2022/edit/main/Memoria/DiseñoFrontend.md "Patrón de diseño")


Arquitectura escogida
-------------

La arquitectura escogida para este servicio es una arquitectura de dos capas, también conocida como Documento-Vista. Estas capas son: Capa de origen de datos y Capa de presentación. 

Eligimos esta opción ya que como la parte de frontend solo nos muestra datos de pega y la presentación de unos documentos html no es necesaria una capa de lógica que trate esos datos. 

La capa de origen de datos corresponde con la carpeta: `dms2122frontend/dms2122frontend/data` 
En esta capa definimos la configuración del frontend y también como vamos a comunicarnos con los otros componentes de la aplicación como el componente auth y el componente backend. 

La capa de presentación corresponde con la carpeta: `dms2122frontend/dms2122frontend/presentation` 
En esta capa definimos toda la presentación que tiene nuestra web. Por ejemplo, es aquí donde comprobamos los roles que tiene cada usuario y dependiendo de esos roles la aplicación le manda a una página u a otra. 

Mecanismos de reutilización
-------------

No hemos utilizado herencia y solo hemos utilizado composición. Se puede observar que no implementamos ni extendemos de ninguna clase para mantener el principio SOLID de Liskov substitution y así no permitir que ningún hijo modifique a ningún padre. 
La composición nos permite tener clases que instancian a otras clases como por ejemplo cuando instanciamos a la clase authservice.py o a la clase responsedata.py.
Hemos utilizado este mecanismo ya que así no violamos el principio SOLID de Single Responsability y asi cada clase tiene su responsabilidad. 

Decisiones referidas a los principios SOLID
-------------

Otra decisión que hemos tomado para mantener algun princpio que estábamos rompiendo en anteriores entregas es la decisión de mover los métodos relativos a la gestión de preguntas y respuestas a la clase `dms2122frontend/dms2122frontend/data/rest/backendservice.py`, esto hace que se mantenga el princpio de responsabilidad única ya que authservice.py tiene su responsabilidad referida a la autenticación y backendservice.py su responsabilidad referida a las preguntas. 

Otra decisión tomada fue la de separar los endpoints del frontend en varias clases diferentes. Cada clase afecta a un rol o componente único (estudiante, profesor, preguntas...) y así mantenemos el principio "Interface segregation" ya que todas las clases dependen de métodos que utilizan.

Patrón de diseño
-------------

Un patrón de diseño que hemos podido introducir es el patrón estructural Fachada. La clase que actúa como fachada es `dms2122frontend/bin/dms2122frontend.py` .
Esto hace que se simplifique el subsitema de endpoints. Todos los endpoints de todas las clases que tenemos en presentation/web se unifican en esta clase y asi simplificamos el acceso a los endpoints. Así cuando queramos acceder a un endpoint nos dirigimos a la fachada y asi no tenemos que conocer la estrcutura interna del subsistema. Con esto desacoplamos el subsistema de endopints de los otros subsistemas.
Esto nos ha simplificado mucho la labor de buscar funcionalidades concretas ya que no teniamos que buscar en 5 archivos si no solo en 1. 







