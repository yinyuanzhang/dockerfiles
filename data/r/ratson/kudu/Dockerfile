FROM ubuntu:xenial

RUN apt-get update && apt-get -y install wget curl && \
cd /etc/apt/sources.list.d && \
wget -qO - https://archive.cloudera.com/cdh5/ubuntu/xenial/amd64/cdh/archive.key | apt-key add - && \
wget http://archive.cloudera.com/kudu/ubuntu/xenial/amd64/kudu/cloudera.list && \
apt-get update && \
apt-get -y install kudu kudu-master kudu-tserver libkuduclient0 libkuduclient-dev && \
apt-get purge -y --auto-remove && \
rm -rf /var/lib/apt/lists/*

VOLUME /var/lib/kudu/master /var/lib/kudu/tserver
EXPOSE 8050 8051 7050 7051

COPY start.sh /
ENTRYPOINT ["/start.sh"]
