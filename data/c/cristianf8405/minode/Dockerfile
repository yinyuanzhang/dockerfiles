#Imagen base
FROM node:latest

#directorio donde van a estor nuestros ficheros
#Directorio de la app
WORKDIR /app


#Copiado de archivos
ADD . /app

#Dependencias
RUN npm install

#Puerto que expongo
EXPOSE 3000

#Comando
CMD ["npm", "start"]
