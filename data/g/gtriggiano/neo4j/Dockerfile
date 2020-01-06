FROM treedom/cron:latest

MAINTAINER Giacomo Triggiano <giacomo@creativecoding.it>

ENV NEO4J_VERSION 2.3.2
ENV NEO4J_EDITION enterprise

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -yq install software-properties-common && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -yq install \
      oracle-java8-installer \
      curl \
      wget && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/oracle-jdk8-installer && \
    wget -O /var/neo4j.tar.gz "http://dist.neo4j.org/neo4j-$NEO4J_EDITION-$NEO4J_VERSION-unix.tar.gz" && \
    tar -xvzf /var/neo4j.tar.gz -C /var && \
    rm /var/neo4j.tar.gz && \
    mv "/var/neo4j-$NEO4J_EDITION-$NEO4J_VERSION" /var/neo4j

RUN mkdir /backups && mkdir /data && rm -rf /var/neo4j/data && ln -s /data /var/neo4j/data

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

COPY /scripts /neo4j

RUN chmod 755 /neo4j/*

VOLUME ["/backups", "/data"]

EXPOSE 7474 6362

CMD ["/neo4j/start"]
