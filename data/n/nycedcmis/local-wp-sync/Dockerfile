FROM node:11
LABEL MAINTAINER="Andrew Lehman <alehman@edc.nyc>"
WORKDIR /usr/src/app
COPY *.json ./
COPY index.js .
COPY modules ./modules
RUN npm install --production
ENTRYPOINT [ "node", "index.js" ]
