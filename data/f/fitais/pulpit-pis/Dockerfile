FROM node:alpine
MAINTAINER Oleksii Filonenko <brightone@protonmail.com>

# server deps
WORKDIR /usr/src/app
COPY ./package*.json ./
RUN npm install

# server
WORKDIR /usr/src/app/server
COPY ./server .

# client deps
WORKDIR /usr/src/app/client
COPY ./client/package*.json ./
RUN npm install

# client
COPY ./client .
RUN npm run build

# run the app
EXPOSE 5000
WORKDIR /usr/src/app/server
CMD ["node", "index.js"]
