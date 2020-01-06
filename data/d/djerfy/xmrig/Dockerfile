FROM ubuntu:18.04
LABEL description="Cryptocurrency XMRig Miner" \
      maintainer="Djerfy <djerfy@gmail.com>"

RUN apt-get update && \
    apt-get install -y git build-essential cmake libuv1-dev libmicrohttpd-dev

RUN git clone https://github.com/xmrig/xmrig.git xmrig && \
    mkdir -p xmrig/build && \
    cd xmrig/build && \
    cmake .. && \
    make && \
    cp xmrig /usr/bin/xmrig

CMD ["/usr/bin/xmrig"]
