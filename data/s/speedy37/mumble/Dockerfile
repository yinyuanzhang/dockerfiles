FROM alpine:3.9

RUN apk add --no-cache murmur \
 && addgroup -S mumble-server && adduser -S mumble-server -G mumble-server
ADD mumble-server.ini /config/mumble-server.ini

VOLUME /data /config
EXPOSE 64738 64738/udp

USER mumble-server
CMD ["/usr/bin/murmurd", "-fg", "-ini", "/config/mumble-server.ini"]
