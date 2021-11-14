# Patrón arquitectónico

Para satisfacer las necesidades que necesita el software se ha elegido un **patrón multicapa** , ya que de esta forma podemos aprovechar las ventajas que nos ofrece este diseño, como minimizar las dependencias y mejorar la encapsulación.

En concreto se va a desarrollar una **arquitectura de 3 capas** :

- **Capa de presentación**

Encargada de proporcionar una interfaz gráfica al usuario para poder hacer uso del software. En nuestro caso se corresponde con el frontend de la aplicación web.

- **Capa de origen de datos**

Se encargará de la comunicación con los sistemas que almacenan los datos, es decir, acceder a ellos, almacenarlos y modificarlos. En nuestro caso se encargará de la comunicación con la base de datos. (En esta entrega no se ha implementado nada de esta capa)

- **Capa de lógica de negocio**

Encargada de toda la lógica interna de la aplicación, por ejemplo, cómo se calculan las notas de los test, qué acciones puede realizar cada usuario dependiendo de su rol, etc.


![esquema del modelo de 3 capas](https://github.com/Alvaro9rc/practica-dms-2021-2022/blob/main/Manuales/img/3capas.png)


En este esquema se puede apreciar cómo se representan las capas y la comunicación entre ellas, nótese que la capa de lógica depende de la de datos, y que se podría comunicar directamente la capa de presentación con la de datos, cuando la lógica de la relación sea simple, por ejemplo podríamos extraer datos y presentarlos en el frontend directamente usando un motor de plantillas como Jinja en Flask.

Aunque el modelo de 3 capas es el que mejor se adapta a nuestra situación, también podría pensarse como un **modelo de 4 capas**.

La nueva capa a incorporar sería la de servicios, que funcionaria sobre la capa de lógica de negocio, y que estaría compuesta de fachadas en su mayor medida que nos permitan la interacción con el servicio desde la aplicación sin tener que preocuparnos del funcionamiento interno, es decir proporcionar una interfaz de acceso a esa funcionalidad. En nuestro caso claramente se ve que se ha aislado un servicio de autenticación, y si la funcionalidad de la aplicación fuese creciendo posiblemente podríamos aislar algún otro servicio más, como por ejemplo, servicio de notificaciones a los usuarios vía correo electrónico o cualquier otra funcionalidad.

De momento no se ve estrictamente necesario pero está bien tenerlo en cuenta para un futuro. Además la ventaja con la que contamos es que adaptar un diseño multicapa de 3 a 4 capas no lleva mucho trabajo y **se podría reutilizar la mayor parte del diseño** anterior.
