FROM alpine:latest

LABEL maintainer "Go Watanabe / gowatana@vmtn.jp"

RUN apk add --no-cache nginx=1.16.1-r0
COPY default.conf /etc/nginx/conf.d/

RUN wget -O- https://github.com/gabrielecirulli/2048/archive/master.zip | unzip -
RUN mv -f 2048-master/* /var/lib/nginx/html/ && rm -rf 2048-master

EXPOSE 80
CMD ["nginx", "-g", "daemon off; pid /run/nginx.pid;"]
