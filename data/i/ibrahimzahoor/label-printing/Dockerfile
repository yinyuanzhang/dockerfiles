FROM node:8

RUN apt-get update
RUN apt-get install -y ghostscript
RUN apt-get install -y pdftk

WORKDIR /usr/src/app
COPY package*.json ./

RUN npm install
COPY . .

EXPOSE 80

CMD [ "npm", "run", "prod:build" ]
CMD [ "npm", "run", "prod:start" ]
