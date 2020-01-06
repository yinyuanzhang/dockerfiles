FROM fedora:23
MAINTAINER Oshan Rube oshanrube@gmail.com

RUN dnf install -y varnish libmhash-devel && \
  dnf clean all

ADD start.sh /start.sh
ADD config/varnish.vcl /etc/varnish/default.vcl

ENV VCL_CONFIG      /etc/varnish/default.vcl
ENV CACHE_SIZE      512m
ENV VARNISHD_PARAMS -p default_ttl=3600 -p default_grace=3600

RUN chmod 777 -R /var/lib/varnish
RUN chown -R 1001:0 /var/lib/varnish

USER 1001

EXPOSE 8081
CMD /start.sh
