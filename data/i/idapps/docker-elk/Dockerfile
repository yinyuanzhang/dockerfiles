FROM ubuntu:14.04

MAINTAINER Javier Fonseca <idapps.ve@gmail.com>

RUN sudo apt-get update
RUN sudo apt-get install -y tar ca-certificates software-properties-common wget build-essential nano pkg-config python-dev python-software-properties

RUN sudo add-apt-repository -y ppa:webupd8team/java
RUN sudo apt-get update
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
RUN sudo apt-get install -y oracle-java8-installer

RUN cd /home && wget https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.1.1/elasticsearch-2.1.1.tar.gz && tar -zxvf elasticsearch-2.1.1.tar.gz
RUN mv /home/elasticsearch-2.1.1 /home/elasticsearch
#RUN ./home/elasticsearch/bin/elasticsearch

RUN cd /home && wget https://download.elastic.co/logstash/logstash/logstash-all-plugins-2.1.0.tar.gz && tar -zxvf logstash-all-plugins-2.1.0.tar.gz
RUN mv /home/logstash-2.1.0 /home/logstash
ADD logstash_simple.conf /home/logstash/logstash_simple.conf
RUN ls /home/logstash
#RUN ./home/logstash/bin/logstash -f logstash_simple.conf

RUN cd /home && wget http://download.elastic.co/kibana/kibana-snapshot/kibana-4.3.1-linux-x64.tar.gz && tar -zxvf kibana-4.3.1-linux-x64.tar.gz && ls /home
RUN mv /home/kibana-4.3.0-linux-x64 /home/kibana
RUN ./home/kibana/bin/kibana

EXPOSE 5601 9200
