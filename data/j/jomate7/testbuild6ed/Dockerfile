# Imagen Origen

FROM node:6.0.0

# Carpeta Raiz
WORKDIR /apitechu

# Copia de archivos de la carpeta local a apitechu
ADD . /apitechu

#si en .dockerignore añadimos ./node_modules pondremos este comando que sigue.
RUN npm install

#Exponer el puerto en el contenedor
EXPOSE 3000

#Comando de inicialización.
CMD ["npm","start"]
