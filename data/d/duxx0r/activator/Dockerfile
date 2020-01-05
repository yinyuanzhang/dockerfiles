# Lightbend Activator

FROM java:8

MAINTAINER @duxx0r

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
  apt-get install -yq wget unzip && \
  apt-get autoremove -yq && \
  apt-get clean -yq && \
  rm -rf /var/lib/apt/lists/*

ENV ACTIVATOR_VERSION 1.3.10
ENV SBT_VERSION 0.13.5

WORKDIR /opt

# Install Activator
RUN wget -q --progress=dot:mega http://downloads.typesafe.com/typesafe-activator/$ACTIVATOR_VERSION/typesafe-activator-$ACTIVATOR_VERSION.zip && \
  unzip -qq typesafe-activator-$ACTIVATOR_VERSION.zip && \
  mv activator-dist-$ACTIVATOR_VERSION /opt/activator && \
  ln -s /opt/activator/bin/activator /usr/local/bin/activator && \
  rm -f typesafe-activator-$ACTIVATOR_VERSION.zip

# Install SBT
RUN wget https://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb
RUN dpkg -i sbt-$SBT_VERSION.deb && \
rm sbt-$SBT_VERSION.deb && \
sbt sbtVersion && \
rm -rf target/

# SBT warmup
#ADD . /var/www
#WORKDIR /var/www/sbt-warmup
#RUN sbt run
#RUN rm -rf ./*
