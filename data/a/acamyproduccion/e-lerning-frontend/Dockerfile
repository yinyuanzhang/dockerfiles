FROM node:8.7.0

#MAINTAINER 

# usar cambios en package.json para forzar a Docker a no usar el caché 
# cuando cambiemos las dependencias de nodejs de nuestra aplicación: 
ADD package.json /tmp/package.json
RUN cd /tmp && npm install
RUN mkdir -p /usr/src/app && cp -a /tmp/node_modules /usr/src/app

# A partir de aquí, cargamos el código de nuestra aplicación, por lo tanto, la "capa" anterior de la ventana acoplable que se almacenó en la memoria caché se utilizará si es posible 

WORKDIR /usr/src/app
ADD . /usr/src/app

RUN npm run build
RUN rm -rf ./build
RUN rm -rf ./test
RUN rm -rf ./src

ENV PORT=80

EXPOSE 80

CMD [ "npm" , "start" ]

