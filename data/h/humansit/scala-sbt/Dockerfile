#
# Scala and sbt Dockerfile
#
# https://github.com/humansit/scala-sbt
#

# Pull base image
FROM findepi/graalvm

# Env variables
ENV SCALA_VERSION 2.12.7
ENV SBT_VERSION 1.0.4

# Scala expects this file
#RUN touch /usr/lib/jvm/java-8-openjdk-amd64/release
RUN \
  echo "Installing CURL" && \
  apt-get update && \
  apt-get install -y curl

# Install Scala
## Piping curl directly in tar
RUN \
  curl -fsL https://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz | tar xfz - -C /root/ && \
  echo >> /root/.bashrc && \
  echo "export PATH=~/scala-$SCALA_VERSION/bin:$PATH" >> /root/.bashrc

# Install sbt
RUN \
  echo "Installing SBT" && \
  curl -L -o sbt-$SBT_VERSION.deb https://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \
  dpkg -i sbt-$SBT_VERSION.deb && \
  rm sbt-$SBT_VERSION.deb && \
  apt-get update && \
  apt-get install -y sbt && \
  sbt sbtVersion

RUN \
  echo "Installing RPM Build tools" && \
  apt-get update && \
  apt-get install -y rpm

RUN \
  echo "Installing git" && \
  apt-get update && \
  apt-get install -y git

RUN \
  echo "Installing python" && \
  apt-get update && \
  apt-get install -y python


RUN \
  echo "Installing pip" && \
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
  python get-pip.py

RUN \
  echo "Installing awscli" && \
  pip install awscli

# Define working directory
WORKDIR /root
