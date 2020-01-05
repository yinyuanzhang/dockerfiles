FROM node:8.9-alpine

# Create app directory
RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app/

RUN npm install

# Build
RUN npm run build 

EXPOSE 3000
CMD [ "npm", "start" ]