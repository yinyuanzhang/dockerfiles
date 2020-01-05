FROM alpine:3.5
RUN   apk update \
      && apk add ca-certificates wget xrefresh xdotool \
      && update-ca-certificates \
      && rm -rf /var/cache/apk/* \
      && wget -q http://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-static.tar.xz \
      && tar xvf ffmpeg-release-64bit-static.tar.xz \
      && cp ffmpeg-*-64bit-static/ffmpeg /usr/local/bin \
      && rm -rf ffmpeg-*-64bit-static*
ENTRYPOINT ["ffmpeg"]
      
      