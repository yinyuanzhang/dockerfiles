FROM alpine
RUN apk upgrade -U -a
RUN apk add --no-cache darkhttpd && mkdir -p /www
EXPOSE 80
VOLUME /www
WORKDIR /www
CMD ["/usr/bin/darkhttpd", "/www", "--chroot", "--uid", "darkhttpd", "--gid", "www-data"]
