FROM node:alpine

RUN apk update && \
    apk add --virtual build-dependencies \
    build-base gcc wget git bash python

RUN npm install -g nodemon

COPY mule /app

WORKDIR /app

VOLUME ['/app']

EXPOSE 9999

CMD ["npm", "run", "dev"]