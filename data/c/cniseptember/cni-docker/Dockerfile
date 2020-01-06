#Specify base image
FROM node:alpine

#Working dir
WORKDIR /usr/app

#Install dependencies
COPY ./package.json ./
RUN npm install
COPY ./ ./

#Default run command
CMD ["npm","start"]
