FROM alpine:3.9

ENV VERSION=4.1.1
ARG MD5SUM="7bce08bcc241f12d40616d09f810883a  ffmpeg-release-amd64-static.tar.xz"
WORKDIR /tmp

RUN wget -q https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz \
 && echo "${MD5SUM}" | md5sum -c \
 && tar xf ffmpeg-release-amd64-static.tar.xz \
 && mv /tmp/ffmpeg-${VERSION}-amd64-static/ffmpeg /usr/local/bin \
 && rm -rf /tmp/*

ENTRYPOINT ["/usr/local/bin/ffmpeg"]
CMD ["--help"]
