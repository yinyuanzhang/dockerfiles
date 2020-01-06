FROM alpine:edge

MAINTAINER Philipp Schmitt <philipp@schmitt.co>

RUN apk add --no-cache stunnel

VOLUME ["/config", "/certs"]

EXPOSE 443

ENTRYPOINT ["/usr/bin/stunnel"]

CMD ["/config/stunnel.conf"]
