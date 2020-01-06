FROM alpine:3.8

RUN apk --no-cache add expat expat-dev openssl openssl-dev wget build-base \
      perl perl-dev perl-app-cpanminus && \
    cpanm JSON::XS && \
    cpanm Paws && \
    rm -rf /root/.cpanm && \
    apk --no-cache del build-base
