# Imagen base de node
FROM node:latest

# Directorio de la app en el contenedor
WORKDIR /app

# Copiado de todos los archivos al raiz del contenedor
ADD . /app

# Dependencias
RUN npm install

# Puerto que expongo
EXPOSE 3000

# Comando con el que se ejecuta la app desde docker
CMD ["npm","start"]
