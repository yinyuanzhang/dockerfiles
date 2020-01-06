FROM node:10-alpine

COPY . .

RUN npm install

RUN npm i -g @adonisjs/cli

RUN ls -la

EXPOSE 3333

CMD [ "npm", "start"]
