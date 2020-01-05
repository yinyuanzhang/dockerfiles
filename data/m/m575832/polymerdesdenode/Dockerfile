# Imagen base
FROM node:latest

# Directorio de la app en el contenedor con el codigo
WORKDIR /app

# Copiado de archivos
ADD /build/default /app/build/default
ADD server.js /app
ADD package.json /app

 # Dependencias
 RUN npm install

 # Puerto que expongo
 EXPOSE 3000

 # Comando con el que se debe ejecutar la appp
 CMD ["npm", "start"]
