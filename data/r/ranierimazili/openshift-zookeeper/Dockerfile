FROM ubuntu:18.04

WORKDIR /opt

ENV ZKP_SERVERS ""
ENV ZKP_ID ""

EXPOSE 2181 2888 3888

#Install zookeeper dependencies
RUN apt-get update

RUN apt-get -y install \
    ca-certificates \
    zip \
    net-tools \
    vim \
    tar \
    netcat \
    curl \
    openjdk-8-jdk 

#Download and uncompress zookeeper binaries
RUN mkdir zookeeper \
    && cd zookeeper \
    && curl -s http://ftp.unicamp.br/pub/apache/kafka/2.2.0/kafka_2.12-2.2.0.tgz | tar -xz --strip-components=1

#Copy config files
COPY build_zookeeper_conf_file.sh /opt
RUN chmod +x /opt/build_zookeeper_conf_file.sh
COPY zookeeper.properties /opt/zookeeper/config/ 

#Create zookeeper data dir
RUN mkdir -p /data/zookeeper

#Set OS proprieties
RUN echo 'vm.swappiness=1' | tee --append /etc/sysctl.conf

#Create the zookeeper user and set permissions
RUN useradd zookeeper
RUN chown -R zookeeper:zookeeper /opt/zookeeper
RUN chown -R zookeeper:zookeeper /data/zookeeper
RUN chown -R zookeeper:zookeeper /opt/build_zookeeper_conf_file.sh

USER zookeeper

CMD /opt/build_zookeeper_conf_file.sh \
    && /opt/zookeeper/bin/zookeeper-server-start.sh zookeeper/config/zookeeper.properties