FROM alpine:latest

MAINTAINER pauluzznl 

RUN apk --update add bind

EXPOSE 53/tcp
EXPOSE 53/udp

RUN mkdir -p /var/named/
RUN chown named:named /var/named/
COPY assets/named-regular.conf /etc/named.conf
COPY assets/example.com.db /var/named/example.com.db

CMD ["named", "-c", "/etc/named.conf", "-g", "-u", "named"]
