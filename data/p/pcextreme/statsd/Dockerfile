FROM node:0.12

ARG STATSD_VERSION=0.8.0
ARG STATSD_CHECKSUM=5868ff01d3f2fa316bf7d9f9ad8e972db2fd963f

MAINTAINER Wido den Hollander <wido@widodh.nl>

RUN apt-get -y update
RUN apt-get install -y curl

RUN mkdir /src \
    && cd /src \
    && curl -SL -o statsd.tar.gz https://github.com/etsy/statsd/archive/v${STATSD_VERSION}.tar.gz \
    && echo "${STATSD_CHECKSUM}  statsd.tar.gz" > sha1sums.txt \
    && sha1sum -c sha1sums.txt \
    && mkdir statsd \
    && tar xvf statsd.tar.gz -C statsd --strip-components=1 \
    && rm sha1sums.txt statsd.tar.gz

RUN mkdir /etc/statsd
ADD config.js /etc/statsd/config.js

EXPOSE 8125/udp 8126

CMD ["node", "/src/statsd/stats.js", "/etc/statsd/config.js"]
