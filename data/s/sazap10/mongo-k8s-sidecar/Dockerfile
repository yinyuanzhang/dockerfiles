FROM node:alpine

WORKDIR /app

COPY package.json package-lock.json /app/

RUN npm install

COPY ./src /app/src

CMD ["npm", "start"]
