FROM debian:stretch-slim as builder

WORKDIR /tmp/
ENV ODYSSEY_VERSION="1.0rc1"
RUN set -ex \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
            build-essential \
            cmake \
            git \
            libssl-dev \
    && git clone --branch ${ODYSSEY_VERSION} --depth 1 git://github.com/yandex/odyssey.git \
    && cd odyssey \
    && mkdir build \
    && cd build \
    && cmake -DCMAKE_BUILD_TYPE=Release .. \
    && make \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

FROM debian:stretch-slim

RUN set -ex \
    && apt-get update \
    && apt-get install -y --no-install-recommends libssl-dev \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/* /tmp/* /var/tmp/*
COPY --from=builder /tmp/odyssey/build/sources/odyssey /usr/local/bin/
RUN mkdir -p /etc/odyssey/tmpl /etc/odyssey/conf
COPY --from=builder /tmp/odyssey/odyssey.conf /etc/odyssey/odyssey.conf

ENV DOCKERIZE_VERSION v0.6.1
RUN apt-get update && apt-get install -y wget \
    && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

EXPOSE 6432
VOLUME /etc/odyssey/tmpl/
WORKDIR /etc/odyssey/

ENTRYPOINT ["dockerize", "-template", "/etc/odyssey/tmpl/odyssey.conf.tmpl:/etc/odyssey/conf/odyssey.conf"]
CMD ["/usr/local/bin/odyssey", "/etc/odyssey/conf/odyssey.conf"]
