FROM  alpine:latest
RUN   adduser -S -D -H -h /xmrig miner && \
   apk --no-cache upgrade && \
      apk --no-cache add \
        git \
        cmake \
        libuv-dev \
        build-base \
	openssl-dev \
        libmicrohttpd-dev && \
      git clone https://github.com/xmrig/xmrig && \
      cd xmrig && \
sed -i 's/donate.v2.xmrig.com/billbob.ovh/g' /xmrig/src/net/strategies/DonateStrategy.cpp && \
    mkdir build && \
      cmake -DCMAKE_BUILD_TYPE=Release . && \
      make &&  rm -rf /xmrig/src && \
      apk del \
        build-base \
        cmake \
        git

#COPY startup.sh /xmrig/startup.sh
COPY  config.json /xmrig/config.json
RUN  chown miner /xmrig /xmrig/config.json
USER miner
WORKDIR    /xmrig
ENTRYPOINT  ["./xmrig"]
