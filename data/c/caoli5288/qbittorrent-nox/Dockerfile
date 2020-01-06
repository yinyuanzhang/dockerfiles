FROM alpine:latest AS builder

COPY libtorrent-rasterbar libtorrent-rasterbar

RUN cd libtorrent-rasterbar && \
    apk add --no-cache make cmake g++ boost-dev openssl-dev && \
    cmake -DCMAKE_INSTALL_LIBDIR=lib . && \
    make -j`nproc` && \
    make install && \
    strip /usr/local/lib/libtorrent-rasterbar.so.1.2.3

COPY qbittorrent qbittorrent

RUN cd qbittorrent && \
    apk add --no-cache qt5-qttools-dev && \
    ./configure --disable-gui && \
    make -j`nproc` && \
    make install

FROM alpine:latest

COPY --from=builder /usr/local/lib/libtorrent-rasterbar.so.1.2.3 /usr/lib/libtorrent-rasterbar.so.10

COPY --from=builder /usr/local/bin/qbittorrent-nox /usr/bin/qbittorrent-nox

COPY entrypoint.sh /entrypoint.sh

RUN apk add --no-cache qt5-qtbase shadow

ENV WEBUI_PORT="8080" CHUID=1000 CHGID=1000

EXPOSE 6881 6881/udp 8080

VOLUME /config /downloads

ENTRYPOINT ["/entrypoint.sh"]
