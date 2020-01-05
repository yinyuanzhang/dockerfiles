#
# Scala and sbt Dockerfile
#
# https://github.com/hseeberger/scala-sbt
#

# Pull base image
FROM ubuntu:18.04

LABEL MAINTAINER Santosh Kumar Talachutla <santosh@prodifyllp.com> <http://go2santosh.com/)
ENV DEBIAN_FRONTEND noninteractive
ENV JAVA_HOME       /usr/lib/jvm/java-8-oracle
ENV LANG            en_US.UTF-8
ENV LC_ALL          en_US.UTF-8


# Env variables
ENV SCALA_VERSION 2.12.8
ENV SBT_VERSION 1.2.8
ENV REDIS_VERSION=5.0.4 

# Installating Java

RUN apt-get update && \
  apt-get install -my wget gnupg2 && \
  apt-get install -y --no-install-recommends locales && \
  locale-gen en_US.UTF-8 && \
  apt-get dist-upgrade -y && \
  apt-get --allow-releaseinfo-change update && \
  apt-get --purge remove openjdk* && \
  apt install -y openjdk-8-jdk && \
 # echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections && \
 # apt-get install -y software-properties-common python-software-properties && \
 # add-apt-repository ppa:webupd8team/java && \
 # apt-get update && \
 # apt-get install -y --no-install-recommends oracle-java8-installer oracle-java8-set-default && \
  apt-get clean all

# Install base dependencies
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y -q --no-install-recommends \
        apt-utils \
        apt-transport-https \
        build-essential \
        ca-certificates \
        curl \
        git \
        libssl-dev \
        python \
        rsync \
        software-properties-common \
        devscripts \
        autoconf \
        ssl-cert \
        systemd \
    && apt-get clean

#Install Supervisor
#RUN apt-get update && apt-get install -y supervisor
#RUN mkdir -p /var/log/supervisor
#COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
#CMD ["/usr/bin/supervisord"]

# update the repository sources list
# and install dependencies
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs

# confirm installation
RUN node -v
RUN npm -v

# Install Docker 
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg |  apt-key add - 
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable" 
RUN apt-get update
RUN apt-cache policy docker-ce
RUN apt-get install -y docker-ce

# Install reactive client
RUN npm i nexe -g 
RUN apt-get install -y -qq \
    ca-certificates \
    clang++-3.9 \
    libgc-dev \
    libunwind8-dev \
    libre2-dev \
    libcurl4-openssl-dev \
    jq 

RUN  wget -qO - https://downloads.lightbend.com/rp/keys/bintray-debian | \
    apt-key add - && \
    echo "deb https://dl.bintray.com/lightbend/deb $(lsb_release -cs) main" | \
    tee /etc/apt/sources.list.d/lightbend.list && \
    apt-get install apt-transport-https -y && \
    apt-get update && \
    apt-get install reactive-cli 

# Install Scala 
## Piping curl directly in tar
RUN \
  curl -fsL https://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz | tar xfz - -C /root/ && \
  echo >> /root/.bashrc && \
  echo "export JAVA_HOME=/" >> /root/.bashrc && \
  echo "export PATH=~/scala-$SCALA_VERSION/bin:$PATH" >> /root/.bashrc 

# Install sbt    
RUN \
  curl -L -o sbt-$SBT_VERSION.deb https://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \
  dpkg -i sbt-$SBT_VERSION.deb && \
  rm sbt-$SBT_VERSION.deb && \
  apt-get update && \
  apt-get install sbt && \
  sbt sbtVersion && \
  mkdir project && \
  echo "scalaVersion := \"${SCALA_VERSION}\"" > build.sbt && \
  echo "sbt.version=${SBT_VERSION}" > project/build.properties && \
  echo "case object Temp" > Temp.scala && \
  sbt compile && \
  rm -r project && rm build.sbt && rm Temp.scala && rm -r target

# Install Redis 
#RUN \
  #apt-get install -y redis-server && \
 # sed -i 's/supervised no/supervised systemd/g' /etc/redis/redis.conf 

# Define working directory
WORKDIR /root
