FROM node:boron

#CREAR DIRECTORIO DE LA APP
ENV carpeta /usr/src/app
RUN mkdir -p carpeta
RUN mkdir -p /usr/src/app/src
WORKDIR /usr/src/app

# Instalar dependencias
#RUN apt-get update
#RUN apt-get install -y --no-install-recommends git
#RUN apt-get clean
#RUN npm install -g gulp bower polymer-cli generator-polymer-init-custom-build
RUN npm install -g bower
RUN npm install -g polymer-cli

RUN bower install polymerelements/iron-ajax --save --allow-root

COPY package.json /usr/src/app

# Empaquetar código
COPY . /usr/src/app
COPY ./src /usr/src/app/src

# Publico el puerto
EXPOSE 8081

# Arranco la aplicacion
CMD [ "polymer" , "serve", "--hostname 0.0.0.0" ]
