FROM alpine:latest
MAINTAINER Michel Belleau <michel.belleau@malaiwah.com>

RUN apk --update add bind

ADD assets/named.conf /etc/bind/named.conf
ADD assets/empty.conf /etc/bind/conf.d/domains.conf
RUN mkdir -p /etc/bind/conf.d/ && chown -R root:named /etc/bind && chmod 0775 /etc/bind

ADD start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 53/udp
EXPOSE 53

CMD ["/start.sh"]
