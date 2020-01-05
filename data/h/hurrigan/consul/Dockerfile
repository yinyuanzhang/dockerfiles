FROM hurrigan/debian:8.4

MAINTAINER David Calvert <dockerhub@hurrigan.com>

ENV CONSUL_VERSION 0.6.4

RUN apt-get update && \
    apt-get install -y ca-certificates unzip wget && \
    wget https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip && \
    wget https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_web_ui.zip && \
    unzip consul_${CONSUL_VERSION}_linux_amd64.zip -d /bin/ && \
    unzip consul_${CONSUL_VERSION}_web_ui.zip -d /ui/ && \
    apt-get autoremove --purge -y unzip wget && \
    rm -rf consul_* /var/lib/apt/lists/*

EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp

VOLUME [ "/data" ]

ENTRYPOINT [ "/bin/consul" ]

CMD [ "agent", "-dev" ]
