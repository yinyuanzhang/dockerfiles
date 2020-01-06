#Imagen base
FROM node:latest

#Directorio de la aplicacion
WORKDIR /app

#Copia de archivos
ADD /build/default /app/build/default
ADD server.js /app
ADD package.json /app

#Dependencias
RUN npm install

#Puerto de trabajo
EXPOSE 3000

#Comando requerido para ejecutarse
CMD ["npm", "start"]

#Version cambiada
