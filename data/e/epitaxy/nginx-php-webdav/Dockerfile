FROM ubuntu:latest
LABEL maintainer="jaeyeol@gmail.com"
RUN apt install bash && \
    apt update && \
    apt -y install nginx-light libnginx-mod-http-dav-ext vim php7.2-fpm php7.2-gd wget
CMD service php7.2-fpm start && nginx -g 'daemon off;'
