FROM isuper/java-oracle:jdk_latest

MAINTAINER Rahul Shukla "rahul@wootag.com"

ENV SCALA_HOME /usr/local/share/scala
ENV PATH $PATH:$SCALA_HOME/bin

ENV SCALA_VERSION 2.11.11
ENV SBT_VERSION 0.13.16

RUN apt-get update && apt-get install wget && \
    wget --quiet http://downloads.lightbend.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz && \
    tar -xf scala-$SCALA_VERSION.tgz && \
    rm scala-$SCALA_VERSION.tgz && \
    mv scala-$SCALA_VERSION $SCALA_HOME

# Install sbt
RUN \
  curl -L -o sbt-$SBT_VERSION.deb https://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \
  dpkg -i sbt-$SBT_VERSION.deb && \
  rm sbt-$SBT_VERSION.deb && \
  apt-get update && \
  apt-get install sbt && \
  sbt sbtVersion

RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN sbt compile
RUN rm -rf /usr/src/app/*  
