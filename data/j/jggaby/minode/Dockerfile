#Imagen base
FROM node:latest

#dicretorio de la app
WORKDIR /app

# copiado de archivos
ADD . /app

#Dependencias
RUN npm install

#Puerto que expongo
EXPOSE 3000

#Comando de ejecuciòn
CMD ["npm","start"]
