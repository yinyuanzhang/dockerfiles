FROM alpine AS tmp
MAINTAINER Rafał Krypa <rafal@krypa.net>

ARG FFMPEG_VERSION=4.1
ARG FFMPEG_URL=https://johnvansickle.com/ffmpeg/releases/ffmpeg-$FFMPEG_VERSION-64bit-static.tar.xz

ADD ${FFMPEG_URL} /tmp/ffmpeg.tar.xz
RUN cd /tmp && tar xJf ffmpeg.tar.xz

FROM scratch

COPY --from=tmp /tmp/ffmpeg*/ffmpeg /bin/

ENTRYPOINT ["/bin/ffmpeg"]
CMD ["--help"]
