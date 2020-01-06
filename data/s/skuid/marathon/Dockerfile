FROM debian:jessie
MAINTAINER Micah Hausler, <hausler.m@gmail.com>

RUN apt-get update \
    && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E56151BF \
    && echo "deb http://repos.mesosphere.com/debian jessie main" | \
     tee /etc/apt/sources.list.d/mesosphere.list \
    && echo "deb http://httpredir.debian.org/debian jessie-backports main" | \
     tee -a /etc/apt/sources.list \
    && apt-get -y update \
    && apt-get -y install \
        openjdk-8-jre-headless \
        mesos \
        marathon \
        unzip \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get autoremove

EXPOSE 8080

CMD ["java", "-jar", "/usr/bin/marathon", "--zk=zk://127.0.0.1:2181/marathon", "--master=zk://127.0.0.1:2181/mesos"]
