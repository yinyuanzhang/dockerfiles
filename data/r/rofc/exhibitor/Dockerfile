FROM openjdk:slim

ENV ZOOKEEPER_VERSION 3.4.13
ENV EXHIBITOR_VERSION 1.7.1

RUN apt-get -y upgrade && \
    apt-get -y update && \
    apt-get install -y curl maven procps 

WORKDIR /exhibitor

COPY entrypoint.sh pom.xml /exhibitor/

RUN curl -o zookeeper-${ZOOKEEPER_VERSION}.tar.gz https://archive.apache.org/dist/zookeeper/zookeeper-${ZOOKEEPER_VERSION}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz && \
    curl -o zookeeper-${ZOOKEEPER_VERSION}.tar.gz.md5 https://archive.apache.org/dist/zookeeper/zookeeper-${ZOOKEEPER_VERSION}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz.md5 && \
    md5sum -c zookeeper-${ZOOKEEPER_VERSION}.tar.gz.md5 && \
    tar xfz zookeeper-${ZOOKEEPER_VERSION}.tar.gz && \
    ln -s zookeeper-${ZOOKEEPER_VERSION} zookeeper && \
    mkdir /exhibitor/zookeeper/data && \
    mvn install && \
    mv target/exhibitor-${EXHIBITOR_VERSION}.jar exhibitor.jar && \
    rm -rf *.tar.gz* pom.xml target/ && \
    chmod +x /exhibitor/entrypoint.sh

EXPOSE 2181 2888 3888 8080

ENTRYPOINT ["/exhibitor/entrypoint.sh"]
