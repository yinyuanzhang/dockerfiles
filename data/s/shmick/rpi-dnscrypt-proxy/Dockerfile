FROM balenalib/raspberry-pi2-alpine

RUN [ "cross-build-start" ]

RUN install_packages coreutils

ENV BASE_URL="https://github.com/jedisct1/dnscrypt-proxy/releases"

WORKDIR /opt/dnscrypt-proxy

RUN FILEVER=$(curl -sL $BASE_URL | grep -v beta | grep -Eo 'dnscrypt-proxy-linux_arm-[0-9.]+[0-9]' | sort -V | tail -n1) && \
    echo "using $FILEVER" && \
    VER=${FILEVER/dnscrypt-proxy-linux_arm-/} && \
    curl -sLO $BASE_URL/download/$VER/${FILEVER}.tar.gz && \
    tar --strip-components=1 -xvzf ${FILEVER}.tar.gz && \
    rm ${FILEVER}.tar.gz

RUN sed "s/^listen_addresses.*/listen_addresses = [':5300']/" example-dnscrypt-proxy.toml > dnscrypt-proxy.toml && \
    sed -i "s/^# server_names.*/server_names = ['google', 'cloudflare']/" dnscrypt-proxy.toml

RUN [ "cross-build-end" ]

EXPOSE 5300/tcp
EXPOSE 5300/udp

ENTRYPOINT ["/opt/dnscrypt-proxy/dnscrypt-proxy"]
CMD ["-config", "/opt/dnscrypt-proxy/dnscrypt-proxy.toml"]
