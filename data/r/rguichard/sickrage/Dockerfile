FROM alpine:3.1

MAINTAINER Romain Guichard <rguichard@vsense.fr>

RUN apk --update add \
    python \
    zip \
    git \
    supervisor
RUN apk --update add --virtual deps \
    python-dev \
    py-pip \
    build-base && \
    pip install cheetah && \
    apk del deps && \
    rm -rf /var/cache/apk/*
RUN git clone https://github.com/SiCKRAGETV/SickRage /sickrage && \
    cd /sickrage && \
    git checkout develop && \
    mkdir -p /data /config && \
    adduser -D -h /sickrage -s /sbin/nologin -u 7001 media && \
    chown -R media:media /sickrage /config /data

WORKDIR /sickrage

VOLUME ["/data"]
VOLUME ["/config/"]

COPY supervisord.conf /etc/supervisord.conf
COPY supervisord-sickrage.ini /etc/supervisor.d/supervisord-sickrage.ini

CMD ["supervisord", "-c", "/etc/supervisord.conf", "-n"]

EXPOSE 8081

