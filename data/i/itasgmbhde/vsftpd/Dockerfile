#vim: set ft=dockerfile:
FROM alpine:3.9
RUN apk add --no-cache vsftpd openssl

ADD vsftpd.conf  /etc/vsftpd/vsftpd.conf
ADD docker-entrypoint.sh /
RUN chmod +x docker-entrypoint.sh

EXPOSE 20 21 10090-10100

ENTRYPOINT ["/docker-entrypoint.sh"]
