FROM busybox:buildroot-2014.02

MAINTAINER Pascha Butretell <admin@pascha.domains>

RUN    adduser -u 3342 -D pascha \
    && mkdir -p /volumes/dweb-data \
    && chown pascha:pascha /volumes/dweb-data \
    && chmod 770 /volumes/dweb-data

VOLUME ["/volumes/dweb-data"]