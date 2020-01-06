FROM senasi/php:7.1

RUN mkdir /data && \
    mkdir /data/temp && \
    mkdir /data/log && \
    chown www-data.www-data /data/temp /data/log

WORKDIR /data
VOLUME /data
