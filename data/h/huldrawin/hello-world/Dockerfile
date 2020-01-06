FROM node:6.9.5-slim

RUN mkdir /app
WORKDIR /app
ADD package.json /app
RUN npm install
ADD index.js docker-entrypoint.sh /app/
EXPOSE 3000
ENTRYPOINT "/app/docker-entrypoint.sh"