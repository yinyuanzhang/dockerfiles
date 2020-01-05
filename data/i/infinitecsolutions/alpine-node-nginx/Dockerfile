FROM node:8-alpine

RUN apk update
RUN apk add nginx gettext libintl
RUN rm -rf /var/cache/apk/* /tmp/*

COPY ./nginx.conf /etc/nginx/nginx.conf

STOPSIGNAL SIGTERM
CMD ["nginx", "-g", "daemon off;"]
