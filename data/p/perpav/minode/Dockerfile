#Imagen bas
FROM node:latest

#Directorio de la app
WORKDIR /app

#Copia de archivos
ADD . /app

#Dependencias
RUN npm install

#Puerto que expongo
EXPOSE 3000

#Comando
cmd ["npm", "start"]
