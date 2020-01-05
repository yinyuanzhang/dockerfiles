FROM debian

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    easy-rsa \
    iptables \
    openvpn \
    tcpdump \
 && rm -rf /etc/openvpn/* \
 && rm -rf /var/lib/apt/lists/*

COPY ./entrypoint.sh /

EXPOSE 1193

ENTRYPOINT ["/entrypoint.sh"]
