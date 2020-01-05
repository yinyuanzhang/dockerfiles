FROM ruby:2.6.1-alpine3.9

LABEL maintainer="nyankokota <public@nyanko-kota.com>"

RUN set -e && \
    apk add --no-cache ruby ruby-bigdecimal ruby-json libstdc++ sqlite-libs && \
    apk add --no-cache --virtual .build-deps ruby-dev make g++ sqlite-dev && \
    gem install mailcatcher --no-document && \
    rm -rf /tmp/* /var/tmp/*

EXPOSE 1025
EXPOSE 8082

CMD ["mailcatcher", "--no-quit", "--foreground", "--ip=0.0.0.0", "--http-port=8082"]
