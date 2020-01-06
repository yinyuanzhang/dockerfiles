# build stage
FROM node:lts-alpine as build-stage
WORKDIR ./
COPY package.json ./
COPY yarn.lock ./

RUN yarn install
COPY . .
RUN yarn build

# production stage
FROM nginx:stable-alpine as production-stage

RUN rm /etc/nginx/conf.d/default.conf

COPY --from=build-stage ./dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 5000

CMD ["nginx", "-g", "daemon off;"]
