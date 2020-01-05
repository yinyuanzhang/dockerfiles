#
# Scala and sbt Dockerfile
#
# https://github.com/hseeberger/scala-sbt
#

# -------------------------------------------------- Pull base image
FROM  python:3.6.4-stretch

ENV SCALA_VERSION 2.11.11
ENV SBT_VERSION 0.13.16

# -------------------------------------------------- Install python packages
RUN pip install Cython==0.28.1 pytest==3.6.3 pytest-cov==2.5.1 coverage==4.3 numpy==1.14.2 awscli

COPY requirements.txt /opt/ci/requirements.txt
RUN pip install -r /opt/ci/requirements.txt && \
    rm /opt/ci/requirements.txt

# -------------------------------------------------- Install jdk 8 and utils

RUN \
  mkdir -p /usr/share/man/man1 && \
  apt-get update && \
  apt-get -y install openjdk-8-jdk=8u212-b01-1~deb9u1 && \
  apt-get -y install jq curl kafkacat git && \
  apt-get -y clean && apt-get -y autoremove

RUN \
 curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-$(uname -s)-$(uname -m) \
 -o /usr/local/bin/docker-compose && \
 chmod +x /usr/local/bin/docker-compose

# -------------------------------------------------- Install Scala

RUN touch /usr/lib/jvm/java-8-openjdk-amd64/release
## Piping curl directly in tar
RUN \
  curl -fsL https://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz | tar xfz - -C /root/ && \
  echo >> /root/.bashrc && \
  echo 'export PATH=~/scala-$SCALA_VERSION/bin:~/bin:$PATH' >> /root/.bashrc

# -------------------------------------------------- Install sbt

RUN \
  curl -L -o sbt-$SBT_VERSION.deb https://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \
  dpkg -i sbt-$SBT_VERSION.deb && \
  rm sbt-$SBT_VERSION.deb && \
  apt-get update && \
  apt-get install sbt && \
  apt-get -y clean && apt-get -y autoremove && \
  sbt sbtVersion


# -------------------------------------------------- Install postgresql && gcc from testing repository

RUN echo 'deb http://ftp.de.debian.org/debian testing main' >> /etc/apt/sources.list
RUN echo 'APT::Default-Release "stable";' | tee -a /etc/apt/apt.conf.d/00local
RUN \
  apt-get update && \
  apt-get -y -t testing install postgresql && \
  apt-get -y -t testing install gcc && \
  apt-get -y clean && apt-get -y autoremove

# -------------------------------------------------- Other stuff

ENV MATPLOTLIBRC="/root"
RUN echo "backend      : Agg" >> $MATPLOTLIBRC/matplotlibrc

COPY initdb /root/bin/
COPY postgres /root/bin/
COPY parse_argument /root/bin/

# Define working directory
WORKDIR /root

# Define entrypoint
ENTRYPOINT /bin/bash

