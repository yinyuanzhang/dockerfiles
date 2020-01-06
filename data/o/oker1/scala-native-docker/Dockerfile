#
# Scala native and sbt Dockerfile, based on https://github.com/hseeberger/scala-sbt
#
# https://github.com/oker1/scala-native-docker
#

# Pull base image
FROM  openjdk:8

ENV SCALA_VERSION 2.12.2
ENV SBT_VERSION 0.13.15

# Scala expects this file
RUN touch /usr/lib/jvm/java-8-openjdk-amd64/release

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
  apt-get install -y clang-3.8 libgc-dev libunwind-dev libre2-dev && \
  sbt sbtVersion

# Define working directory
WORKDIR /root
