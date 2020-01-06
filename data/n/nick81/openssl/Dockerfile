FROM gliderlabs/alpine:3.1

MAINTAINER Nick Bergmann

RUN apk-install openssl

ADD openssl.cnf /etc/ssl/openssl.cnf
ADD bootstrap.sh /home/root/bootstrap.sh

RUN chmod +x /home/root/bootstrap.sh

WORKDIR /app

ENTRYPOINT ["/home/root/bootstrap.sh"]
CMD ["version"]
