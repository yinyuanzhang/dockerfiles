# Image base
FROM node:latest

#Directorio de la app del contenedor
WORKDIR /app

#Copiado del archivos
ADD /build/default /app/build/default
ADD server.js /app
ADD package.json /app

# Dependencias
RUN npm install

# Puerto que expongo
EXPOSE 3000

# Comando con el que ejecutará  la aplicación
CMD ["npm","start"]
