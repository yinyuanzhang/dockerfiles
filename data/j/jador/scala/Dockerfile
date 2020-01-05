FROM jeanblanchard/busybox-java:jdk8

MAINTAINER Tyler Graham <tyler.graham.prog@gmail>

WORKDIR /usr/local/share

RUN opkg-install bash && curl http://downloads.typesafe.com/scala/2.11.6/scala-2.11.6.tgz | gunzip -c | tar x

ENV SCALA_HOME /usr/local/share/scala-2.11.6

ENV PATH $PATH:$SCALA_HOME/bin
