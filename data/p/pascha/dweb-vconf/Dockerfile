FROM busybox:buildroot-2014.02

MAINTAINER Pascha Butretell <admin@pascha.domains>

RUN    adduser -u 3342 -D pascha \
    && mkdir -p /volumes/dweb-conf \
    && chown pascha:pascha /volumes/dweb-conf \
    && chmod 770 /volumes/dweb-conf

VOLUME ["/volumes/dweb-conf"]