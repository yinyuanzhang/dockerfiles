FROM node:10-alpine

RUN npm i -g express
RUN npm i -g express-generator

RUN express /app
WORKDIR /app

RUN npm i
RUN npm i --save mongoose body-parser moment

CMD ["npm", "start"]
