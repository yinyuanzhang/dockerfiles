FROM node:dubnium-alpine

WORKDIR /

COPY . .

RUN npm install --quiet

ENV TYPE=docker

EXPOSE 5000

CMD [ "npm", "start"]
