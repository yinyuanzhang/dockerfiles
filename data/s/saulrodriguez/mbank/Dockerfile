# Imagen base
FROM node:latest

# Directorio de la app:
WORKDIR /app

# Copiado de archivos
ADD build/default /app/build/default
ADD server.js /app
ADD package.json /app

# Dependecias
RUN npm install

# Puerto que expongo
EXPOSE 3000

# Comando para ejecutar la aplicacion
CMD ["npm", "start"]
