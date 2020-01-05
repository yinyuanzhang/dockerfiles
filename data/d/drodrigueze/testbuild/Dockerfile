# Imagen origen
FROM node:6.0.0

# Carpeta raíz
WORKDIR /apitechu

# Copia de archivos de la carpeta local a apitechu
ADD . /apitechu
###RUN npm install -> se trae las dependencias en el momento de generar la imagen

# Exponer puerto
EXPOSE 3000

# Comando de inicialización
CMD ["npm","start"]
###CMD ["RUN","npm","install"] -> se ejecuta una vez instanciado la imagen
