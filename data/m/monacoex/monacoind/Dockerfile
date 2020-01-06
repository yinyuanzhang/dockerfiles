FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:visvirial/monacoin && \
    apt-get update && \
    apt-get install -y monacoind=0.17.1-bionic2 && \
    apt-get remove -y software-properties-common && \
    apt-get autoremove -y && \
    rm -r /var/lib/apt/lists /var/cache/apt

EXPOSE 9401 9402 29000
VOLUME /root/.monacoin

ENTRYPOINT [ "/usr/bin/monacoind" ]
