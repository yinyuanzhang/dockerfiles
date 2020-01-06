#Imagen Base
FROM node:latest

#Directorio de la app
WORKDIR /app

#copia de archivos
ADD . /app
#Dependecias
RUN npm install

#Puerto que expongo
EXPOSE 3000

#Comando
CMD ["npm","start"]