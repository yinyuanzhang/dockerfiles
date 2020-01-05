FROM ubuntu:16.04
MAINTAINER Andrea Lorenzetti <andrea@ibuildings.it>

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

RUN deps=" \
    software-properties-common \
    " && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get upgrade -y $deps --no-install-recommends && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    apt-get install -y oracle-java8-installer oracle-java8-set-default && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/oracle-jdk8-installer

WORKDIR /data

CMD ['bash']
