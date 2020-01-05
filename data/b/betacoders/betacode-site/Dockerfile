FROM node:8.11.2-alpine as node

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

FROM httpd:2.4

COPY --from=node /usr/src/app/dist/ /usr/local/apache2/htdocs/