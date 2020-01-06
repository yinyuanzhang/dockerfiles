#Image base 
FROM node:latest

#Directorio de la app en el contenedor
WORKDIR /app

#Copiado de archivos
ADD . /app

#Dependencias
RUN npm install

#Puerto que exponga
EXPOSE 3000

#Comando 
CMD ["npm","start"]
