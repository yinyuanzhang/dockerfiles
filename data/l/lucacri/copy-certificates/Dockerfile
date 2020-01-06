FROM lucacri/alpine-base:3.10
LABEL maintainer="lucacri@gmail.com"

ADD rootfs /
RUN apk upgrade --update-cache && \
    apk update && \
    apk add bash  && \
    rm -rf /var/cache/apk/* && \
    chmod +x /etc/services.d/notifier/run



ENV DOMAIN_NAME="domain"

VOLUME ["/from", "/to"]
