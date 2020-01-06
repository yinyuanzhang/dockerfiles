FROM alpine:3.10.1
RUN apk upgrade --no-cache
RUN apk add git=2.22.0-r2 \
    --repository https://nl.alpinelinux.org/alpine/edge/main \
    --no-cache
ENTRYPOINT ["/bin/sh"]
