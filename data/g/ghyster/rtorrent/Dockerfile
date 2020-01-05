FROM alpine:edge
MAINTAINER ghyster <nicolas.legras@gmail.com>
## Prepare ##
ENV TERM xterm
RUN apk add --update rtorrent && \
    mkdir ~/session

# Port 49164 is opening incoming connections from other peers.
# Port 6881 is the DHT port if you wish to use it.
# Port 5000 is used for XML/RPC
EXPOSE 49164 6881 5000
# These volumes are mostly optional it depends on how you want to run your container.
VOLUME ["/data/complete", "/data/incomplete", "/data/watch", "/data/added", "/data/downloads", "/data/torrents"]
#ENTRYPOINT  ["rtorrent"]
CMD  ["rtorrent"]
