FROM node:8.12.0

WORKDIR /usr/src/app

COPY dist ./dist
COPY package.json ./package.json

RUN npm install

EXPOSE 3000
CMD [ "npm", "run", "start" ]
