FROM ubuntu:16.04

MAINTAINER Laurent RICHARD "easylo@gmail.com"

RUN apt-get update --fix-missing
RUN apt-get upgrade -y
RUN apt-get -y install supervisor varnish

COPY supervisor/ /etc/supervisor/conf.d/
RUN chmod a+x -R /etc/supervisor/conf.d/scripts/

COPY conf/default.vcl /etc/varnish/default.vcl
# COPY conf/varnishncsa /etc/default/varnishncsa
COPY conf/varnishncsa.service /etc/systemd/system/varnishncsa.service

ENV VARNISH_BACKEND_PORT 80
ENV VARNISH_BACKEND_IP 127.0.0.1
ENV VARNISH_PORT 80
ENV VARNISHNCSA_LOGFORMAT "%h %l %u %t \"%m %U%q %H\" %s %b \"%{Referer}i\" \"%{User-agent}i\" %D \"%{Host}i\" \"%{X-Forwarded-For}i\" \"%{X-Forwarded-Proto}i\" %{Varnish:hitmiss}x"
ENV VARNISHNCSA_LOGPATH /var/log/varnish/varnishncsa.log

EXPOSE 80

# Expose volumes to be able to use data containers
VOLUME ["/var/lib/varnish", "/etc/varnish"]


CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
