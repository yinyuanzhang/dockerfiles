#Imagen base
FROM node:latest

#Dierctorio de la app
WORKDIR /app

#Copiado de archivos
ADD . /app

#Dependencias
RUN npm install

#Puerto que expongo
EXPOSE 3000

#Comando
CMD ["npm", "start"]
