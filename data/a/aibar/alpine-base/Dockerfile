FROM alpine:3.4

COPY repositories /etc/apk

RUN apk update && \
    apk upgrade && \
    apk add ca-certificates && \
    apk add libssl1.0 && \
    apk add curl && \
    rm -rf /var/cache/apk/*