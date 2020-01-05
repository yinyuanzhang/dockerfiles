## base image
#FROM node:12.11.1
#
## set working directory
#WORKDIR /Hoover
#
## add `/usr/src/app/node_modules/.bin` to $PATH
##ENV PATH /StatusUpdater/node_modules/.bin
##:$PATH
##MKDIR /StatusUpdater
#COPY . /Hoover
#
## install and cache app dependencies
#RUN ls
#RUN cd client && npm install && npm run-script build
#RUN npm install
##RUN npm install react-scripts@1.1.1 -g --silent
#
## start app
#CMD ["node", "app.js"]



FROM mongo

RUN apt-get update
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - \
    && apt-get install -y nodejs

#set working directory
WORKDIR /Hoover
COPY . /Hoover

# install and cache app dependencies
#RUN ls
RUN cd client && npm install && npm run-script build
RUN npm install
#RUN npm install react-scripts@1.1.1 -g --silent

# start app
CMD ["./start.sh"]

EXPOSE 3001
