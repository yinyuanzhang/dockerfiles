# Imagen base
FROM node:latest

# Directorio de la app en el contenedor
WORKDIR /app

# Copiado de archivos - Todos los archivos se van al directorio raiz del contenedor
ADD . /app

# Dependencias - Que cuando se cree la imagen descargue todas las dependencias
RUN npm install

# Puerto que expongo - Debe ser el mismo del server.js
EXPOSE 3000

# Comando con el que debe ejecutar docker la aplicacion
CMD ["npm", "start"]
