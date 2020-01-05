FROM alpine:3.2

RUN apk --update add bash dnsmasq

RUN rm -rf /tmp/* /var/cache/apk/*

RUN mkdir /config && chown root:root /config

ADD bin/start /bin/start
RUN chmod a+x /bin/start

EXPOSE 53
VOLUME ["/config"]

ENV SHELL /bin/bash

ENTRYPOINT ["/bin/start"]