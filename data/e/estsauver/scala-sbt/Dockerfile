#
# Scala and sbt Dockerfile
#
# https://github.com/estsauver/scala-sbt
#

# Pull base image
FROM  openjdk:8

ENV SCALA_VERSION 2.12.7
ENV SBT_VERSION 1.2.6

# Scala expects this file
RUN touch /usr/lib/jvm/java-8-openjdk-amd64/release

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs

# Install Scala
## Piping curl directly in tar
RUN \
  curl -fsL http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz | tar xfz - -C /root/ && \
  echo >> /root/.bashrc && \
  echo 'export PATH=~/scala-$SCALA_VERSION/bin:$PATH' >> /root/.bashrc

# Install sbt
RUN \
  curl -L -o sbt-$SBT_VERSION.deb http://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \
  dpkg -i sbt-$SBT_VERSION.deb && \
  rm sbt-$SBT_VERSION.deb && \
  apt-get update && \
  apt-get install sbt && \
  sbt 'set scalaVersion := "2.11.8"' compile

RUN apt-get install python

RUN \
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
  python get-pip.py

RUN pip install awscli

# Define working directory
WORKDIR /root
