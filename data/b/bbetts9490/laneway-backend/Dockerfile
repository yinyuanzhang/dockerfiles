# create a file named Dockerfile
FROM node:lts-alpine

RUN mkdir /app

WORKDIR /app

COPY package.json /app

RUN npm install

COPY . /app

EXPOSE 5000

CMD ["npm", "start"]
