FROM node:11

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install --only=prod

COPY . .

EXPOSE 4390
CMD ["npm", "start"]