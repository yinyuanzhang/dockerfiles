FROM node:alpine

RUN npm i -g livescript
RUN npm i -g pug-cli
RUN npm i -g stylus

RUN npm i -g jstransformer-livescript
RUN npm i -g jstransformer-pug
RUN npm i -g jstransformer-stylus

RUN mkdir /build

WORKDIR /build

CMD ["lsc"]








