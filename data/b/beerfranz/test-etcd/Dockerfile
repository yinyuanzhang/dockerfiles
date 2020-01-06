FROM debian:stable-slim

ENV ETCDCTL_API 3

RUN apt-get update && apt-get install -y wget libcurl3 procps net-tools openssl ca-certificates iputils-ping && mkdir -p /appli/etcd
RUN wget -q https://github.com/etcd-io/etcd/releases/download/v3.3.10/etcd-v3.3.10-linux-amd64.tar.gz
RUN tar xzf etcd-v3.3.10-linux-amd64.tar.gz && mv etcd-v3.3.10-linux-amd64/* /appli/etcd
RUN rm etcd-v3.3.10-linux-amd64.tar.gz

EXPOSE 2379 2380
COPY ./entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
