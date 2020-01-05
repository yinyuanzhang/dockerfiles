FROM balenalib/raspberry-pi-debian-node as builder

ENV VERSION 2.3.0

RUN [ "cross-build-start" ]

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
            git python3-sphinx \
            build-essential erlang libicu-dev \
            libmozjs185-dev libcurl4-openssl-dev \
            ca-certificates curl

RUN git clone https://github.com/apache/couchdb.git -b ${VERSION} --depth 1 \
    && cd couchdb \
    && ./configure --disable-docs --disable-fauxton \
    && make && make release

RUN [ "cross-build-end" ]

FROM balenalib/raspberry-pi-debian-node

RUN [ "cross-build-start" ]

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
               curl libmozjs185-1.0 \
               libc6 libcurl3 libgcc1 libicu57 \
               libssl1.0.2 libstdc++6 libtinfo5 \
    && rm -rf /var/lib/apt/lists/*

RUN [ "cross-build-end" ]

COPY --from=builder /couchdb/rel/couchdb /
COPY raspberry-pi/debian/couchdb/default.ini /etc/

CMD /bin/couchdb
