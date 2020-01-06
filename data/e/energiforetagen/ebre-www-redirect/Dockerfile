FROM nginx:alpine

EXPOSE 80

RUN \
  apk update && \
  apk add ca-certificates && \
  rm -rf /var/cache/apk/*

COPY default.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf
