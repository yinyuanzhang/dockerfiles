FROM alpine:3.3

ENV ANOPE_VERSION=2.0.3

RUN adduser -D ircd -s /bin/false ircd

RUN apk --update add \
  ca-certificates cmake gcc g++ libc-dev make openssl-dev tar wget \
  && rm -rf /var/cache/apk/*

COPY config.cache /

RUN wget https://github.com/anope/anope/releases/download/$ANOPE_VERSION/anope-$ANOPE_VERSION-source.tar.gz \
  && tar xvf anope*.tar.gz \
  && rm -f anope*.tar.gz

RUN cd anope* \
  && cp /config.cache . \
  && ./Config -quick \
  && cd build \
  && make

RUN cd anope*/build \
  && make install
