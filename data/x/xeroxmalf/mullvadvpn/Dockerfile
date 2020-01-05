FROM alpine:latest
RUN \
    echo "**** install packages ****" && \
    apk --no-cache --no-progress add bash curl unzip tar iptables ip6tables jq openvpn && \
    echo "**** add s6 overlay ****" && \
    curl -o /tmp/s6-overlay.tar.gz -L \
        "https://github.com/just-containers/s6-overlay/releases/download/v1.21.7.0/s6-overlay-amd64.tar.gz" && \
    tar xfz /tmp/s6-overlay.tar.gz -C / && \
    echo "**** cleanup ****" && \
    apk del --purge tar && \
    rm -rf /tmp/*

COPY root/ /

ENTRYPOINT ["/init"]