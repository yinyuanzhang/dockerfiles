FROM node:10.15.1-alpine as node

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build:prod

FROM nginx:alpine

COPY ./nginx.conf /etc/nginx/nginx.conf

WORKDIR /usr/share/nginx/html

COPY --from=node /usr/src/app/dist/apelon-ts-browser .

CMD ["nginx", "-g", "daemon off;"]