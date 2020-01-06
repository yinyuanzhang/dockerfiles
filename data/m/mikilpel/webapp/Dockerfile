FROM gliderlabs/alpine:latest

RUN apk-install nginx && mkdir /tmp/nginx

COPY public /usr/share/nginx/html

EXPOSE 80
ENV DISCOVER web-server:80


CMD ["nginx", "-g", "daemon off; error_log stderr info;"]