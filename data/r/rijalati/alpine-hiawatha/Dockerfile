FROM alpine:latest
MAINTAINER rijalati@gmail.com

RUN apk update \
    && apk add curl mbedtls mbedtls-static mbedtls-utils mbedtls-dev --update-cache --repository http://dl-8.alpinelinux.org/alpine/edge/community/  --allow-untrusted \
    && apk add hiawatha hiawatha-doc --update-cache --repository http://dl-8.alpinelinux.org/alpine/edge/testing/ --allow-untrusted

ENTRYPOINT ["hiawatha"]
