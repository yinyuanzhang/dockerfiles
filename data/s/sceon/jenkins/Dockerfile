FROM debian:jessie

RUN echo "deb http://repos.mesosphere.io/debian jessie main" > /etc/apt/sources.list.d/mesosphere.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \
    apt-get -y update && \
    apt-get install -y --no-install-recommends \
    default-jre-headless \
    wget \
    mesos && \
    rm -rf /var/lib/apt/lists/* && \
    echo manual > /etc/init/mesos-slave.override && \
    echo manual > /etc/init/mesos-master.override

WORKDIR /jenkins
ADD download.sh ./download.sh
RUN ./download.sh

ADD . ./

WORKDIR /jenkins/home

ENV JAVA_HOME="/usr/lib/default-java"

ENTRYPOINT ["/jenkins/docker-entrypoint.sh"]
