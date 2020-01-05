FROM alpine:3.10.1
RUN apk upgrade --no-cache
RUN apk add haproxy=2.0.3-r0 \
    --repository https://nl.alpinelinux.org/alpine/edge/main \
    --no-cache
#VOLUME /etc/haproxy
STOPSIGNAL SIGUSR1
ENTRYPOINT ["haproxy", "-db"]
CMD ["-f", "/etc/haproxy"]
