# Imagen a partir de la imagen oficial de Node con Alpine
FROM node:10-alpine

# Información del autor
LABEL maintainer='Iván Garzón (ivangs98@gmail.com)'

# Creamos el directorio de trabajo de nuestro proyecto
WORKDIR /gymmanager

ENV PORT 8080

# Copiamos los archivos necesarios para el funcionamiento de la aplicación
COPY package.json ./
COPY src ./src
COPY gulpfile.js ./

# Instalamos las dependencias del proyecto
RUN npm install

# Eliminamos las dependencias que no son necesarias en producción
RUN npm prune --production

# Instalamos gulp, que es la herramienta de construcción principal
RUN npm install -g gulp

CMD ["gulp", "start-simple"]

EXPOSE 8080