FROM alpine:3.5

LABEL MAINTANER='Glesio Paiva <glesio@gmail.com>'

ENV VERSION 0.20.6
ENV URL 'http://localhost:1313'

RUN apk add --no-cache curl && \
    mkdir /tmp/hugo && \
    curl -L https://github.com/spf13/hugo/releases/download/v${VERSION}/hugo_${VERSION}_Linux-64bit.tar.gz | tar xvz -C /tmp/hugo && \
    mv /tmp/hugo/hugo /usr/local/bin && \
    rm -rf /tmp/hugo && \
    apk del curl && \
    mkdir /hugo

VOLUME /hugo
WORKDIR /hugo
EXPOSE 1313

CMD hugo server -b ${URL} --bind=0.0.0.0
