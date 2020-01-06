FROM alpine:3.10

RUN apk add --no-cache ffmpeg python && mkdir /download && \
    wget https://yt-dl.org/downloads/latest/youtube-dl \
      -O /usr/local/bin/youtube-dl && \
    chmod a+rx /usr/local/bin/youtube-dl

ENV FORMAT="bestvideo[fps<=30][ext=mp4]+bestaudio[ext=m4a]"
ENV PROXY=socks5://shadowsocks:1080
ENV OUTPUT_FORMAT=mp4
ENV VIDEO_URL=""
ENV ARGS=""

WORKDIR /download

ADD run.sh /

ENTRYPOINT ["/run.sh"]
CMD ["/run.sh", "dl"]

