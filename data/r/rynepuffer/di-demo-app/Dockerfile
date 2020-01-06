FROM node:8.7.0

WORKDIR /usr/src/app

COPY package.json .

RUN npm install -g yarnpkg && yarn install

COPY . .

EXPOSE 8080:8080

CMD ["yarn", "start"]
