FROM alpine:latest

RUN apk add --no-cache cups

CMD ["/usr/sbin/cupsd", "-f"]

EXPOSE 631

VOLUME ["/etc/cups"]

