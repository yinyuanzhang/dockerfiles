FROM debian:8.6

ENV GOGS_CUSTOM=/data/gogs \
    USERNAME=root

VOLUME /data

EXPOSE 22 3000

ENTRYPOINT ["/gogs/gogs", "web"]

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install git \
                    wget \
                    ca-certificates \
                    openssh-client -y --no-install-recommends && \
    apt-get clean && \
    wget http://dl.bintray.com/walkingdevs/mirrors/gogs-0.8.43.tar.gz -O /gogs.tar.gz && \
    tar xf /gogs.tar.gz -C / && \
    rm -rf /gogs.tar.gz