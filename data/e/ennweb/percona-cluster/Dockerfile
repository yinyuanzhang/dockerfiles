FROM ubuntu:xenial

MAINTAINER Emre <e@emre.pm>

ENV DEBIAN_FRONTEND noninteractive
ENV PERCONA_RELEASE_VERSION 0.1-4
ENV PERCONA_VERSION 57
ENV SERVER_ID 1

RUN \
    apt-get update && \
    apt-get install -y --no-install-recommends apt-transport-https ca-certificates pwgen vim wget xinetd curl jq && \
    wget https://repo.percona.com/apt/percona-release_${PERCONA_RELEASE_VERSION}.xenial_all.deb && \
    dpkg -i percona-release_${PERCONA_RELEASE_VERSION}.xenial_all.deb && \
    rm -rf percona-release_${PERCONA_RELEASE_VERSION}.xenial_all.deb && \
    apt-get update && \
    apt-get install -y percona-xtradb-cluster-${PERCONA_VERSION} && \
    rm -rf /var/lib/apt/lists/*

ADD entrypoint.sh /
ADD clustermon /usr/bin
RUN chmod a+x /entrypoint.sh /usr/bin/clustermon

VOLUME ["/var/lib/mysql", "/var/log/mysql"]

EXPOSE 3306 4567 4568 9200

ENTRYPOINT ["/entrypoint.sh"]
