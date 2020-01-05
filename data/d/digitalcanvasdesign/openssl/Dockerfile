FROM alpine:3.6

LABEL maintainer="Jason Raimondi <jason@raimondi.us>"

RUN apk update && \
    apk add --no-cache openssl && \
    rm -rf /var/cache/apk/*

ENTRYPOINT ["openssl"]
