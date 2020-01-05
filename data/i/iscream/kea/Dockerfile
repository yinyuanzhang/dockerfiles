FROM debian:stretch-slim as builder
ENV KEA_VERSION 1.5.0
RUN apt update && \
    apt install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        curl \
        libssl-dev \
        liblog4cplus-dev \
        libboost-all-dev \
        automake \
        libtool \
        pkg-config && \
    curl -LO https://ftp.isc.org/isc/kea/${KEA_VERSION}/kea-${KEA_VERSION}.tar.gz && \
    tar xzvf kea-${KEA_VERSION}.tar.gz -C /usr/local/src && \
    cd /usr/local/src/kea-${KEA_VERSION} && \
    ./configure --with-openssl --with-log4cplus && \
    make && \
    make install

FROM debian:stretch-slim
COPY --from=builder /usr/local/ /usr/local/

RUN apt update && \
    apt install -y --no-install-recommends \
        libssl1.1 \
        liblog4cplus-1.1-9 && \
    apt autoremove -y && \
    rm -rf /var/cache/apt/* /var/lib/{cache,apt,log,dpkg} && \
    ldconfig && \
    mkdir /etc/kea /var/kea

EXPOSE 67/udp
EXPOSE 547/udp
CMD ["/usr/local/sbin/keactrl", "start", "-c", "/etc/kea/keactrl.conf"]
