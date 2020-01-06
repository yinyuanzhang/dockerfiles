FROM alpine:3.8

LABEL maintainer "Harpo Roeder <roederharpo@protonmail.ch>"

RUN apk add ffmpeg python

ADD https://yt-dl.org/downloads/latest/youtube-dl /usr/local/bin/youtube-dl

RUN chmod a+rx /usr/local/bin/youtube-dl

WORKDIR /ctx

VOLUME ["/ctx"]

ENTRYPOINT ["youtube-dl"]
