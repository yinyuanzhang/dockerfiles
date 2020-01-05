FROM lsiobase/alpine:3.10

RUN set -xe \
    && apk add --no-cache ca-certificates \
                          ffmpeg \
                          openssl \
                          python3 \
    && pip3 install youtube-dl
    
WORKDIR /

RUN ["/bin/bash", "-c", "echo I am now using bash!"]
