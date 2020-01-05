##########################################################################
# Image: ptylr/alpine:3.5
# Maintained by: Paul Taylor <me@ptylr.com>
##########################################################################
FROM alpine:3.5
MAINTAINER Paul Taylor <me@ptylr.com>

ENV REFRESHED_AT "2017-02-04"
ENV HOME "/usr/local/ptylr"
ENV KEEPALIVE_TAIL "-f /dev/null"

ADD ./conf/opt/container/initcontainer /opt/container/
RUN mkdir -p /scratch \
        /usr/local/ptylr/ \
        /opt/container && \
    chmod u+x /opt/container/initcontainer && \
    apk add --update bash && \
    rm -rf /var/cache/apk/*

ENTRYPOINT [ "/bin/bash", "/opt/container/initcontainer" ]