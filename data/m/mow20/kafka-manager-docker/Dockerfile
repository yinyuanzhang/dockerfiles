FROM centos:7

MAINTAINER Clement Laforet <sheepkiller@cultdeadsheep.org>

RUN yum update -y && \
    yum install -y java-1.8.0-openjdk-headless && \
    yum clean all

ENV JAVA_HOME=/usr/java/default/ \
    ZK_HOSTS=localhost:2181 \
    KM_VERSION=1.3.3.21 \
    KM_REVISION=b16f88a911701feaec46494c0fc60681ec37f5ff \
    KM_CONFIGFILE="conf/application.conf"

ADD start-kafka-manager.sh /kafka-manager-${KM_VERSION}/start-kafka-manager.sh
ADD sbt-launch.jar /root/.sbt/launchers/0.13.9/sbt-launch.jar
ENV SBT_OPTS="$SBT_OPTS -Dhttp.proxyHost=myhost -Dhttp.proxyPort=myport"
RUN yum install -y java-1.8.0-openjdk-devel git wget unzip which && \
    mkdir -p /tmp && \
    cd /tmp && \
    git clone https://github.com/mow20/kafka-manager && \
    cd /tmp/kafka-manager && \
    git checkout ${KM_REVISION} && \
    echo 'scalacOptions ++= Seq("-Xmax-classfile-name", "200")' >> build.sbt && \
    ./sbt clean dist && \
    unzip  -d / ./target/universal/kafka-manager-${KM_VERSION}.zip && \
    rm -fr /tmp/* /root/.sbt /root/.ivy2 && \
    chmod +x /kafka-manager-${KM_VERSION}/start-kafka-manager.sh && \
    yum autoremove -y java-1.8.0-openjdk-devel git wget unzip which && \
    yum clean all

WORKDIR /kafka-manager-${KM_VERSION}

EXPOSE 9000
ENTRYPOINT ["./start-kafka-manager.sh"]