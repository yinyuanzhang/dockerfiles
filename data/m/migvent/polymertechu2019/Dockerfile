#Imagen base
FROM node:latest

#Directorio de la app
WORKDIR /app

#Copiar los archivos del build
ADD /build/default /app/build/default
ADD server.js /app
ADD package.json /app

#Dependencias
RUN npm install

#puerto que expongo
EXPOSE 3002

#Comando de ejecucion
CMD ["npm","start"]
