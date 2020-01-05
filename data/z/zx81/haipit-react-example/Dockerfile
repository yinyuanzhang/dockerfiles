FROM node:alpine as builder
COPY . /app
WORKDIR /app
RUN yarn --production
RUN yarn build

FROM nginx:alpine
COPY  --from=builder /app/nginx.conf /etc/nginx/nginx.conf
COPY  --from=builder /app/build/ /usr/share/nginx/html