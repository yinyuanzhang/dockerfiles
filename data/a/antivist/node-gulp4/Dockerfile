FROM node:11.15.0-alpine

COPY package*.json ./
COPY . .

RUN npm install
RUN npm install -g gulp@4.0.0
RUN npm install -g gulp-cli

CMD [ "bash" ]