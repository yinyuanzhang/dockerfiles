# Stage 1
FROM node:8-alpine as node

WORKDIR /usr/src/app

COPY package* ./
COPY yarn* ./
COPY .babelrc ./

RUN npm i

COPY ./src ./src

RUN npm run build

# Stage 2
FROM nginx:alpine

COPY --from=node /usr/src/app/dist /usr/share/nginx/html

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]