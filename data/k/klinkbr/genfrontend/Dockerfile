FROM node:12-alpine

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json /usr/src/app/
COPY yarn.lock /usr/src/app/
RUN yarn install

# Env
ENV API_URL https://genlandpage.klink.ai/api
# ENV API_URL http://192.168.15.14:9090/api

# Bundle app source
COPY . /usr/src/app
RUN yarn generate

# Clear the cache
RUN yarn cache clean

# Install http server
RUN npm i -g http-server

EXPOSE 8080
CMD [ "http-server", "./dist" ]
