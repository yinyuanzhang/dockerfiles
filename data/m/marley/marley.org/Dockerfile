FROM node:alpine as builder

RUN apk update && apk upgrade && \
  apk add --no-cache bash vim less


RUN mkdir -p /project
WORKDIR '/project'

COPY ./package*.json .
RUN npm install

COPY . .

CMD ["npm", "run", "start"]