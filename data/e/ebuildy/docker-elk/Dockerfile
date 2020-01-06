FROM phusion/baseimage:0.9.19

ARG DEBIAN_FRONTEND=noninteractive
ARG LANG=C.UTF-8
ARG ES_VERSION=5.0.0-alpha5
ARG KIBANA_VERSION=5.0.0-alpha5-amd64

RUN echo oracle-java9-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee /etc/apt/sources.list.d/webupd8team-java.list && \
    echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886


RUN set -x && \
    apt-get update && \
    apt-get install -y \
        oracle-java9-installer && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/deb/elasticsearch/${ES_VERSION}/elasticsearch-${ES_VERSION}.deb && \
    wget https://download.elastic.co/kibana/kibana/kibana-${KIBANA_VERSION}.deb

RUN dpkg -i elasticsearch-${ES_VERSION}.deb && \
    dpkg -i kibana-${KIBANA_VERSION}.deb

RUN rm -rf /usr/share/doc /etc/init.d/*

ADD elasticsearch               /etc/service/elasticsearch
ADD elasticsearch/config.yml    /etc/elasticsearch/elasticsearch.yml
ADD elasticsearch/jvm.options   /etc/elasticsearch/jvm.options
ADD kibana                      /etc/service/kibana

EXPOSE 9200
EXPOSE 5601

WORKDIR /usr/share
