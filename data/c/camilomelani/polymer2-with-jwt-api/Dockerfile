# Image base
FROM node:latest

# Directorio de la app
WORKDIR /app

# Copiado de Archivos
ADD build/default /app/build/default
ADD server.js /app
ADD package.json /app


# Dependencias
RUN npm install

#Puerto que expongo
EXPOSE 3002

# Comandos
CMD ["npm", "start"]
