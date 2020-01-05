## Cargamos la imagen de base de linux que usaremos
#bajaremos ubuntu con el TAG 12.04

FROM ubuntu:12.04 

##Actualizamos el sistema y repos

RUN apt-get update

## Instalamos el servidor web

RUN apt-get install -y nginx

##Creamos un Volumen
VOLUME ["/usr/share/nginx/www/"]

##Agregaremos un Argumento para decidir cual instalar, en el caso tenemos dos carpetas 
##web y web1 que serán los argumentos, no olvidar que cuando construimos la imagen
##debemos poner --build-arg webpage=webX

ARG webpage

##Agregamos un directorio
ADD $webpage /usr/share/nginx/www/


##Iniciamos nginx con ENTRYPOINT para que no sea modificado

ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]

##Exponemos el puerto 80

EXPOSE 80


