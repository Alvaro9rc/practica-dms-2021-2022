# FRONTEND


## Patrón arquitectónico

Para satisfacer las necesidades que necesita el software se ha elegido un **patrón multicapa**, ya que de esta forma podemos aprovechar las ventajas que nos ofrece este diseño, como minimizar las dependencias y mejorar la encapsulación.

En concreto se va  a desarrollar una **arquitectura de 2 capas, Document-View**:



* **Capa de presentación**

    Encargada de proporcionar una interfaz gráfica al usuario para poder hacer uso del software. En nuestro caso se corresponde con el frontend de la aplicación web.

* **Capa de origen de datos**

    Se encargará de la comunicación del frontend con los sistemas que almacenan los datos, es decir, acceder a ellos, almacenarlos y modificarlos. En nuestro caso se encargará de la comunicación con la base de datos. 


En este esquema se puede apreciar cómo la capa de presentación depende de la de datos, y que se podría comunicar directamente la capa de presentación con la de datos, cuando la lógica  de la relación sea simple, por ejemplo podríamos extraer datos y presentarlos en el frontend directamente usando un motor de plantillas como Jinja en Flask.


## Principios de diseño SOLID

El principio de single responsibility está o debería de estar presente en todo el código fuente, de forma que cada parte tenga una funcionalidad concreta y diferenciada del resto.

El principio Open/Closed se manifiesta en el uso del motor de plantillas, pudiendo definir una plantilla html base, cerrada, común en todos los casos, pero permitiendo ser extensible para poder así ser aprovechada con distintos propósitos.

El principio de interface segregation, en nuestro caso está pendiente de mejorarse, ya que en alguna clase se incorpora un mix de funcionalidades que se podrían subdividir en varios archivos y así cumplir este principio. Un ejemplo podría ser el uso que hacemos en los endpoints, definiendo en teacherendpoints.py los propios del profesor, en otro archivo los del alumno, etc.


## Patrones estructurales

Las clases webauth, webquestion, webuser y webutil nos están ofreciendo unas fachadas con las que podemos interactuar con el servicio de backend. No están proporcionando una interfaz unificada como tal entre todas las partes, pero podrían verse similitudes.


# BACKEND

Para satisfacer las necesidades que necesita el software se ha elegido un **patrón multicapa**, ya que de esta forma podemos aprovechar las ventajas que nos ofrece este diseño, como minimizar las dependencias y mejorar la encapsulación.

En concreto se ha implementado un **modelo de 3 capas o Negocio.**



* **Capa de presentación**

    Se corresponde con las funcionalidades propias del backend que van a ser usadas por en la capa de presentación del frontend. 


    (Nótese que en nuestro código fuente no se ha implementado nada en esta capa, pero se tendrá en cuenta en las próximas entregas)

* **Capa de origen de datos**

    En esta capa está implementado todo lo referente a la base de datos, es decir, las tablas que la componen están definidas según las especificaciones del orm, así como los métodos encargados de realizar consultas/introducir/actualizar datos en la base de datos. 

* **Capa de lógica de negocio**

    En esta capa se debe de introducir la lógica (es decir el conjunto de reglas o algoritmos que se deben de cumplir) de las operaciones referentes al funcionamiento de la actividad principal de la aplicación, es decir alta/baja/modificación de preguntas, respuesta/visualización de preguntas, gestión de acceso por roles, etc.


    La implementación está hecha, pero se encuentra desorganizada en la estructura de ficheros de la aplicación.



## Principios de diseño SOLID

El principio de single responsibility está o debería de estar presente en todo el código fuente, de forma que cada parte tenga una funcionalidad concreta y diferenciada del resto.

El principio Open/Closed se ve aplicado a la hora de definir las clases, ya que hay que ir pensando en dejarlas más o menos cerradas a su modificación, pero poder abrirlas a su extensión en un futuro si fuese necesario.



## Patrones estructurales

Se podría decir que para la conexión con la base de datos se está empleando un proxy, ya que se mantiene una referencia de acceso a el cliente de bd, nos permite crear conexiones, destruirlas, realizar consultas, etc.


## Patrones de comportamiento

Con lo referente al cambio de roles de los usuarios, podemos aplicar el patrón estado, ya que dependiendo del rol, que puede cambiar dinámicamente también, cada usuario tendrá distintas funcionalidades.
