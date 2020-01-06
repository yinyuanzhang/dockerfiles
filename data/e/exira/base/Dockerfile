FROM alpine:3.4

MAINTAINER exira.com <info@exira.com>

# Add s6-overlay and go_dnsmasq
ENV S6_OVERLAY_VERSION=v1.18.1.3 \
    GODNSMASQ_VERSION=1.0.6

RUN apk update && \
    apk upgrade && \
    apk add --update --no-cache ca-certificates wget bind-tools && \
    update-ca-certificates && \
    wget https://github.com/just-containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-amd64.tar.gz -O /tmp/s6-overlay.tar.gz && \
    tar xvfz /tmp/s6-overlay.tar.gz -C / && \
    rm -f /tmp/s6-overlay.tar.gz && \
    wget https://github.com/janeczku/go-dnsmasq/releases/download/${GODNSMASQ_VERSION}/go-dnsmasq-min_linux-amd64 -O /bin/go-dnsmasq && \
    chmod +x /bin/go-dnsmasq && \
    apk del wget && \
    rm -rf /var/cache/apk/*

ADD root /

ENTRYPOINT ["/init"]
CMD []
