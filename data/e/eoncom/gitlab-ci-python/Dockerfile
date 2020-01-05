FROM alpine:3.9
LABEL maintainer="hoenirvili <hoenirvili@gmail.com>" \
    version="0.1" \
    purpose=ci
RUN apk update && apk upgrade --no-cache && \
    apk add python3 --update-cache --repository http://nl.alpinelinux.org/alpine/edge/community
RUN python3 -m pip install --upgrade pip setuptools wheel
