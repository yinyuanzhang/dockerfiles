FROM linuxserver/lazylibrarian:latest
ENV SET_SERVICE="lazylibrarian"
RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install --no-cache-dir -U crudini && \
    apt-get -y purge python3-pip && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*
COPY s6.lakkris/ /
