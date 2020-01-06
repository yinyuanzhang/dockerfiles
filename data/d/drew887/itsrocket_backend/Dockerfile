##Create a muilti stage image for building node-gyp things
FROM node:11-alpine as bcrypt

WORKDIR /home/node/app

COPY . /home/node/app/

RUN apk --no-cache --virtual deps add \
    python \
    make \
    g++ \
    && npm install \
    && apk del deps

## Start real image

FROM node:11-alpine

WORKDIR /home/node/app

COPY --from=bcrypt /home/node/app/ /home/node/app/

EXPOSE 3000

RUN chown node:node /home/node/ -R

USER node

CMD ./startup.sh
