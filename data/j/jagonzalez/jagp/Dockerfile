#Imagen origen. Si no indicamos nada coge la versión latest
FROM node:6.0.0

# Carpeta raiz
WORKDIR /jagp-techu

# Copia de archivos de la carpeta local a apitechu
ADD . /jagp-techu

# Si en el .dockerignore añadimos ./node_modules
# Poner esto
RUN npm install


# Exponer puerto
EXPOSE 3000

# Comando de inicialización
CMD npm start
