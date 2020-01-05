FROM ubuntu:xenial

RUN apt-get update \
 && apt-get -y install wget curl \
 && cd /etc/apt/sources.list.d \
 && wget -qO - https://archive.cloudera.com/cdh5/ubuntu/xenial/amd64/cdh/archive.key | apt-key add - \
 && wget http://archive.cloudera.com/kudu/ubuntu/xenial/amd64/kudu/cloudera.list \
 && apt-get update \
 && apt-get -y install kudu kudu-master kudu-tserver

ENTRYPOINT ["/bin/bash"]
