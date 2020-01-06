FROM node:13-alpine

ENV \
    YOUTUBEDL_VERSION=2019.11.05 \
    STREAMLINK_VERSION=1.2.0

RUN apk add --no-cache curl python3 python3-dev ca-certificates bash git build-base libgomp ffmpeg && \
    git clone https://github.com/ytdl-org/youtube-dl.git /tmp/youtube-dl && \
    cd /tmp/youtube-dl && python3 setup.py install && \
    git clone https://github.com/streamlink/streamlink.git /tmp/streamlink && \
    cd /tmp/streamlink && python3 setup.py install && \
    git clone https://github.com/back-to/generic.git /tmp/generic && \
    mkdir -p /root/.config/streamlink/ && \
    mv /tmp/generic/plugins /root/.config/streamlink/ && \
    git clone https://github.com/jrudess/streamdvr.git /app && \
    cd /app && \
    echo "Currently on commit:" $(git rev-parse --short HEAD && git log -1 --pretty=%B) && \
    npm install && \
    npm cache clean --force && \
    apk del git python3-dev build-base && \
    rm -rf /tmp/*

WORKDIR /app

VOLUME /app/config /app/capturing /app/captured

RUN chown 1000:1000 -R /app

USER node

CMD ["node", "streamdvr"]

STOPSIGNAL SIGINT
