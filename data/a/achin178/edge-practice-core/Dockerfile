# Base image nodejs
FROM node:8
# Create app directory
RUN mkdir -p /usr/src/app
# Base image nodejs
FROM node:8 as build
# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
# Install app dependencies
COPY package.json /usr/src/app/
RUN npm install
COPY . /usr/src/app

FROM node:8-alpine
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
# Bundle app source
# COPY --from=build . /usr/src/app
COPY --from=build /usr/src/app /usr/src/app
EXPOSE 8080
CMD [ "npm", "start" ]