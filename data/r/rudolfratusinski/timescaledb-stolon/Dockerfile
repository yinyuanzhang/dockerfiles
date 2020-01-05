FROM timescale/timescaledb:latest-pg11-bitnami

USER 0
RUN useradd -ms /bin/bash stolon

RUN set -ex \
    && mkdir -p /build \
    && git clone https://github.com/sorintlab/stolon /build/stolon \
    && cd /build/stolon \
    && git checkout v0.13.0 \
    && wget https://dl.google.com/go/go1.12.7.linux-amd64.tar.gz \
    && tar -C /usr/local -xzf go1.12.7.linux-amd64.tar.gz \
    && export PATH=$PATH:/usr/local/go/bin \
    && go version \
    && go get -v github.com/sorintlab/stolon/cmd \
    && ./build \
    && cd /build/stolon \
    && mv /build/stolon/bin/* /usr/local/bin/ \
    && rm -rf /build/stolon ~/go

RUN chmod +x /usr/local/bin/stolon-keeper /usr/local/bin/stolon-sentinel /usr/local/bin/stolon-proxy /usr/local/bin/stolonctl