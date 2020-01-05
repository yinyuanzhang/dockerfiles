###########################################################
#
# Dockerfile for docxtemplater-webservice-docker
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

COPY package.json $APP
RUN npm install

# Bundle app source
COPY . $APP
COPY ./docxtemplater-js/js/ $APP/node_modules/docxtemplater/js/
# COPY ./docxtemplater-js/img-js/js/ $APP/node_modules/docxtemplater-image-module/js/
COPY ./docxtemplater-js/chart-js/js/ $APP/node_modules/docxtemplater-chart-module/js/

# Env variables
ENV SERVER_PORT 3000

# Expose 3000
EXPOSE 3000

# Startup
ENTRYPOINT node standalone.js