# Imagen origen
FROM node:6.0.0

#Carpeta raiz
WORKDIR /apitechu

# Copia de archivos de la carpeta local a apitechu
ADD . /apitechu

#Si en .dockerignore añadimos ./node_modules
RUN npm install

# Exponer puerto
EXPOSE 3000

#Comando de inicialización
CMD ["npm", "start"]
