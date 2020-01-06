FROM node:alpine
MAINTAINER bram@smout.net

WORKDIR /meshcentral
ENV NODE_ENV=production
RUN apk update
RUN npm install meshcentral 
RUN npm install otplib
RUN npm install @davedoesdev/fido2-lib

EXPOSE 80 443 4443

ENTRYPOINT node "./node_modules/meshcentral"
