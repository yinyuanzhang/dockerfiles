FROM node:alpine as build

WORKDIR /tmp/myapp
COPY myapp .

RUN npm install && npm run build

FROM nginx:alpine as runtime
COPY --from=0 /tmp/myapp/dist /usr/share/nginx/html