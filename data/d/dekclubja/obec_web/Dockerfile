# base image
FROM node:10.8.0

# set working directory
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# install and cache app dependencies
RUN npm install 
RUN npm install -g bower
RUN bower install --allow-root

# start app
# CMD ["npm", "start"]
