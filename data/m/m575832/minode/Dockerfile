# Imagen base
FROM node:latest

# Directorio de la app en el contenedor con el codigo
WORKDIR /app

# Copiado de archivos
ADD . /app

 # Dependencias
 RUN npm install

 # Puerto que expongo
 EXPOSE 3000

 # Comando con el que se debe ejecutar la app
 CMD ["npm", "start"]
