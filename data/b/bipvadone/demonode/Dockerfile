#Imagen base
FROM node:latest

#DIrectorio de la app en el contenedor
WORKDIR /app

#Copiado de archivos
#anade todos los archivos de deonde s estoy al contenedor raiz del docker
ADD . /app

#Dependencias
RUN npm install

#Puerto que expongo
EXPOSE 3000

#Comando
CMD ["npm","start"]
