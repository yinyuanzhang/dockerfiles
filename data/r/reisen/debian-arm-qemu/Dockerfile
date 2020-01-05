FROM arm32v7/debian:latest AS add-apt-repositories

FROM resin/armv7hf-debian-qemu

RUN [ "cross-build-start" ]

RUN apt-get update; \
    apt-get -y dist-upgrade

COPY --from=add-apt-repositories /etc/apt/sources.list /etc/apt/sources.list

RUN apt-get update \
 && apt-get -y dist-upgrade

RUN apt-get -y autoremove \
 && apt-get -y clean \
 && rm -rf /var/lib/apt/lists/*

RUN [ "cross-build-end" ]
