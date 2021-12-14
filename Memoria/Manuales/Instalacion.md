# Manual de instalación y ejecución.

A continuación vamos a detallar los pasos que hay que seguir para instalar y ejecutar la plataforma desarrollada.

## Paso 1: Descarga e instalación de Ubuntu: 

Vamos a descargar e instalar una version de linux ya que es el entorno en el que está desarrollada la plataforma. 
Para ello descargamos un programa que nos permita crear máquinas virtuales como por ejemplo Virtual Box. 
https://www.virtualbox.org/wiki/Downloads.
Lo siguiente que vamos a hacer es descargar Ubuntu para instalarlo en una máquina virtual. 
#### `Ubuntu 20.04.3 LTS`
Link: https://ubuntu.com/download/desktop.

## Paso 2: Instalación entorno: 

Una vez tengamos instalado el sistema operativo vamos a preparar el entorno para poder usar docker y python sin ningún problema. 
Para ello vamos a ejecutar este script:
https://gist.github.com/Kencho/b3829dd99c2c41c9f7a0c854b41dcaf4
Usamos el comando `chmod +x bootstrap.sh` para dar permisos de ejecución al script y lo ejecutamos `sudo bash bootstrap.sh`. 

## Paso 3: Descarga del proyecto: 

A continuación vamos a clonar este repositorio para tenerlo en la máquina virtual. Para ello podemos descargarlo desde el propio github usando la opción descargar como zip 
o con el comando `https://github.com/Alvaro9rc/practica-dms-2021-2022.git`

## Paso 4: Instalación y ejecución del proyecto: 

Por último, una vez tengamos el proyecto descargado en nuestro ordenador, vamos a instalarlo con el comando `docker-compose -f docker/config/dev.yml build` situandonos 
en la carpeta descargada. 
Hecho esto ya tenemos construidas las imágenes y para ejecutar la plataforma usamos el comando `docker-compose -f docker/config/dev.yml up -d`. 
Una vez los contenedores estén corriendo nos dirigimos al enlace http://172.10.1.30:8080/login para poder usar la plataforma.

## Paso 5: Eliminación de contenedores 

Una vez usada la plataforma, para eliminar los contenedores y apagar el servidor, usamos el comando `docker-compose -f docker/config/dev.yml rm -sfv`
Esto cerrara todos los contendores y recursos y habremos finalizado la ejecución de la plataforma.
