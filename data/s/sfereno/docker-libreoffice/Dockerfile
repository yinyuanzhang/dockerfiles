###########################################################
#
# Dockerfile for libreoffice-docker
#
###########################################################

# Setting the base to nodejs 4.2
FROM mhart/alpine-node:4

# Maintainer
MAINTAINER Geir Gåsodden

#### Begin setup ####

ENV APP=/src/app

RUN mkdir -p $APP

WORKDIR $APP

# Install app dependencies
COPY package.json $APP

RUN apk update && apk add libreoffice-common libreoffice-writer libxfont libfontenc ttf-freefont ttf-ubuntu-font-family && apk del libreoffice-gnome

RUN npm install

#ENV NODE_PATH=/src/node_modules

# Bundle app source
COPY . $APP

# Env variables
ENV SERVER_PORT 9001

# Expose 9001
EXPOSE 9001

# Startup
ENTRYPOINT node standalone.js