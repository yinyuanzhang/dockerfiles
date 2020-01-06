FROM alpine:edge AS build
RUN echo http://nl.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
RUN apk add --no-cache gst-rtsp-server-dev libtool gcc musl-dev
COPY examples /src
RUN mkdir /binaries
WORKDIR /binaries
RUN libtool --mode=link \
 gcc `pkg-config --cflags --libs gstreamer-1.0` \
 -L/usr/lib/x86_64-linux-gnu -lgstrtspserver-1.0 \
 -o rtsp-launch /src/test-launch.c

RUN libtool --mode=link \
 gcc `pkg-config --cflags --libs gstreamer-1.0` \
 -L/usr/lib/x86_64-linux-gnu -lgstrtspserver-1.0 \
 -o rtsp-record /src/test-record.c

FROM alpine:edge
RUN echo http://nl.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
RUN apk add --no-cache gst-rtsp-server gst-plugins-base gst-plugins-ugly gst-plugins-good gst-plugins-bad gst-libav

# todo
COPY --from=build /binaries/* /usr/bin/
COPY rtsp-server.sh /

EXPOSE 8554

CMD ["/rtsp-server.sh"]

