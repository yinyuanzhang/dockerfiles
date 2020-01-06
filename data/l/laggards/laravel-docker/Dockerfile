FROM node:latest

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json /usr/src/app/
# Bundle app source
COPY laravel-echo-server.json /usr/src/app/laravel-echo-server.json
RUN npm install -g laravel-echo-server

EXPOSE 6001
CMD [ "laravel-echo-server", "start" ]
