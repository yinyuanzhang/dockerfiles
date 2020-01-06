FROM centos:7.5.1804
MAINTAINER Mike Mester <mike@mester.io>
RUN yum update -y && yum install java-1.8.0-openjdk-devel git sbt epel-release unzip -y
RUN yum install supervisor python-pip -y
WORKDIR /opt
RUN curl -LOJ https://dl.bintray.com/sbt/rpm/sbt-1.2.3.rpm && yum localinstall sbt-1.2.3.rpm  -y
WORKDIR /root/
RUN git clone https://github.com/pndaproject/example-applications.git
RUN git clone https://github.com/yahoo/kafka-manager.git
WORKDIR /root/kafka-manager
RUN sbt clean dist
RUN mv /root/kafka-manager/target/universal/kafka-manager-1.3.3.21.zip /opt
WORKDIR /root/example-applications/flink-streaming-host-network-data-usage/data-source/src/main/resources
RUN pip install -r requirements.txt && mkdir /root/data_gen && cp src.py /root/data_gen/ && cp dataplatform-raw.avsc /root/data_gen/
WORKDIR /opt
RUN unzip kafka-manager-1.3.3.21.zip
RUN curl -LOJ https://archive.apache.org/dist/kafka/1.0.1/kafka_2.11-1.0.1.tgz
RUN tar -zxvf kafka_2.11-1.0.1.tgz
COPY application.conf /opt/kafka-manager-1.3.3.21/conf/application.conf
COPY kafka.supervisor.ini /etc/supervisord.d/kafka_broker.ini
COPY zookeeper.supervisor.ini /etc/supervisord.d/zookeeper_server.ini
COPY kafka-manager.ini /etc/supervisord.d/kafka-manager.ini
COPY kafka-generator.ini /etc/supervisord.d/kafka-generator.ini
RUN rm -rf /root/kafka-manager
EXPOSE 9000



