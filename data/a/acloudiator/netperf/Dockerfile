FROM alpine:latest

MAINTAINER Aasif Shaikh (acloudiator@gmail.com)

ENV NETPERF_VERSION=2.7.0

RUN apk add --no-cache --virtual build-dependencies curl build-base linux-headers lksctp-tools-dev \
    && apk add --no-cache --virtual runtime-dependencies lksctp-tools \
    && curl -LO https://github.com/HewlettPackard/netperf/archive/netperf-${NETPERF_VERSION}.tar.gz \
    && tar -xzf netperf-${NETPERF_VERSION}.tar.gz \
    && cd netperf-netperf-${NETPERF_VERSION} \
    && ./configure --prefix=/usr --enable-histogram --enable-unixdomain --enable-dccp --enable-omni --enable-exs --enable-sctp --enable-intervals --enable-spin --enable-burst --enable-cpuutil=procstat \
    && make \
    && strip -s src/netperf src/netserver \
    && install -m 755 src/netperf src/netserver /usr/bin \
    && rm -rf netperf-${NETPERF_VERSION}* \
    && apk del build-dependencies

EXPOSE 12865

ENTRYPOINT ["/usr/bin/netserver"]

CMD ["-4"]
