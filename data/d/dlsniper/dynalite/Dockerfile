FROM ubuntu:16.04
MAINTAINER Florin Patan

EXPOSE 4567

ENV DYNALITE_VERSION=1.2.0

RUN apt-get update && apt-get install -y g++ \
        make \
        python \
        software-properties-common \
        wget
RUN wget -qO- https://deb.nodesource.com/setup_6.x | bash - && \
    apt-get update && \
    apt-get install -y nodejs
RUN wget -O dynalite.tar.gz https://github.com/mhart/dynalite/archive/v${DYNALITE_VERSION}.tar.gz && \
    tar -xf dynalite.tar.gz -C /tmp/ && \
    rm -f /tmp/dynalite.tar.gz
WORKDIR /tmp/dynalite
RUN npm install -g dynalite && \
    apt-get purge -y g++ \
        make \
        software-properties-common \
        wget && \
    apt-get -y autoremove && \
    apt-get clean && rm -rf /build && rm -rf /tmp/* /var/tmp/* && rm -rf /var/lib/apt/lists/*

CMD ["/usr/bin/dynalite","--createTableMs=100","--deleteTableMs=100","--updateTableMs=100"]
