#Imagen base
FROM node:latest

#Directorio de la app dentro del contenedor donde pondremos la aplicación.
WORKDIR /app

#Copiado de archivos #todo desde la ubicación actual a '/app'
ADD . /app

#Dependencias necesarias par ejecutar la aplicación
RUN npm install

#Puerto que se expone, en éste caso el mismo en que corre la aplicación.
EXPOSE 3000

#Variables de entorno, en éste caso no aplica.

#Comando
CMD ["npm", "start"]
