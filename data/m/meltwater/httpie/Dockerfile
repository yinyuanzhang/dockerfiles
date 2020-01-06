FROM alpine:3.7

RUN apk --no-cache add \
    ca-certificates \
    httpie \
    bash \
    jq \
 && addgroup -g 1000 httpie \
 && adduser -D -G httpie -s /bin/bash -u 1000 httpie

USER httpie
WORKDIR /home/httpie

ENTRYPOINT ["http"]

