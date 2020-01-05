FROM alpine:3.11.2
MAINTAINER Sebastian Braun <sebastian.braun@fh-aachen.de>
# base alpine template

RUN apk --no-cache add exim libcap && \
    mkdir -p /var/spool/exim && \
    ln -sf /dev/stdout /var/log/exim/mainlog && \
    ln -sf /dev/stderr /var/log/exim/panic && \
    ln -sf /dev/stderr /var/log/exim/reject && \
    chown -R exim:exim /var/log/exim /var/spool/exim /usr/lib/exim && \
    chmod 0755 /usr/sbin/exim && \
    setcap CAP_NET_BIND_SERVICE=+eip /usr/sbin/exim

COPY exim.conf /etc/exim/exim.conf

USER exim
EXPOSE 25

ENV SMTP_HOST= \
    SMTP_PORT= \
    SMTP_TLS= \
    SMTP_EMAIL= \
    SMTP_USERNAME= \
    SMTP_PASSWORD= \
    SMTP_CATCHALL=

ENTRYPOINT ["/usr/sbin/exim", "-bdf", "-q15m"]
