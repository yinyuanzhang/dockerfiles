FROM node:10-alpine

RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app

WORKDIR /home/node/app

ENV PATH /home/node/app/node_modules/.bin:$PATH

COPY package*.json ./

RUN apk --no-cache --virtual build-dependencies add \
    python \
    make \
    g++ \
    && npm install \
    && apk del build-dependencies

#RUN apk update \
#    && apk add wget tar file xz
#
#RUN apk update \
#    && apk add alpine-sdk
#
#RUN apk --no-cache --virtual  build-dependencies add \
#    python \
#    make \
#    g++ \
#    && npm install \
#    && apk del build-dependencies
#
#RUN wget https://www.imagemagick.org/download/ImageMagick.tar.gz && \
#    tar -xzf ImageMagick.tar.gz && \
#    cd ImageMagick-7.0.9-10 && \
#    ./configure && \
#    make && \
#    make install && \
#    ldconfig /usr/local/lib && \
#    cd .. && \
#    rm -rf  ImageMagick*


USER node

RUN npm install

RUN mkdir -p /home/node/app/logs

COPY --chown=node:node . .

EXPOSE 4000

EXPOSE 3050

CMD [ "node", "app.js" ]
