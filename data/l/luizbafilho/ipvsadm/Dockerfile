FROM alpine:latest
MAINTAINER Luiz Filho <luizbafilho@gmail.com>

RUN apk add ipvsadm --update-cache --repository http://dl-4.alpinelinux.org/alpine/edge/testing/ --allow-untrusted && rm -rf /var/cache/apk/*

CMD ["/bin/sh"]

