FROM debian:wheezy

ENV ES_VERSION=elasticsearch-1.6.0
ENV JAVA_UPDATE_VERSION=45
ENV JAVA_BUILD_VERSION=14

RUN apt-get update && apt-get install -y curl \
    && mkdir -p /tmp/src \
    && cd /tmp/src \
    && curl -L -O https://download.elastic.co/elasticsearch/elasticsearch/${ES_VERSION}.tar.gz \
    && tar -zxvf ${ES_VERSION}.tar.gz \
    && mkdir -p /usr/share/elasticsearch \
    && cp -ra ${ES_VERSION}/* /usr/share/elasticsearch \
    && curl -L --header "Cookie: oraclelicense=accept-securebackup-cookie;" -O http://download.oracle.com/otn-pub/java/jdk/8u${JAVA_UPDATE_VERSION}-b${JAVA_BUILD_VERSION}/jre-8u${JAVA_UPDATE_VERSION}-linux-x64.tar.gz \
    && tar -zxvf jre-8u${JAVA_UPDATE_VERSION}-linux-x64.tar.gz \
    && mkdir -p /usr/share/java \
    && cp -ra jre1.8.0_${JAVA_UPDATE_VERSION}/* /usr/share/java \
    && apt-get --purge autoremove -y curl && apt-get clean \
    && rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* /usr/share/java/man

ENV JAVA_HOME=/usr/share/java

EXPOSE 9200

WORKDIR /usr/share/elasticsearch/

CMD ["/usr/share/elasticsearch/bin/elasticsearch"]