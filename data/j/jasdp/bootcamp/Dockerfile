FROM node:boron
# Crear directorio de la app
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Instalar dependencias
COPY package.json /usr/src/app
RUN npm install

# Empaquetar código
COPY . /usr/src/app
#
#CREAR DIRECTORIO DE LA APP
#
ENV carpeta /usr/src/app
RUN mkdir -p carpeta
WORKDIR /usr/src/app
#
# Instalar dependencias
#
COPY package.json /usr/src/app
RUN npm install
#
# Empaquetar código
#
COPY . /usr/src/app
#
# Publico el puerto
#
EXPOSE 8081
#
# Arranco la aplicacion
#
CMD [ "npm" , "start" ]
