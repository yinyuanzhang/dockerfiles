FROM alpine

WORKDIR /root

RUN apk --no-cache add tzdata oniguruma
RUN apk --no-cache add --virtual build-dependencies gcc autoconf automake libtool libc-dev oniguruma-dev make git \
 && git clone https://github.com/stedolan/jq \
 && cd jq \
 && autoreconf --install \
 && ./configure --disable-maintainer-mode \
 && make \
 && make install \
 && cd .. \
 && rm -fr jq \
 && apk del build-dependencies

ENTRYPOINT ["jq"]
