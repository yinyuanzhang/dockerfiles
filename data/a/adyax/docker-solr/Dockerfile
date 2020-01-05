# Docker Adyax
#
#

FROM debian:wheezy

MAINTAINER Benoît GRUNENBERGER <bgrunenberger@adyax.com>

ENV DEBIAN_FRONTEND noninteractive


RUN apt-get update -y && \
    apt-get install -y wget tar openjdk-7-jdk openjdk-7-jre && \
    apt-get update -y && \
    apt-get -y autoclean && \
    apt-get -y autoremove && \
	wget http://mir2.ovh.net/ftp.apache.org/dist/lucene/solr/4.9.0/solr-4.9.0.tgz

RUN tar -C /opt --extract --file solr-4.9.0.tgz && \
	mv /opt/solr-4.9.0 /opt/solr && \
	echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections

EXPOSE 8983

WORDIR /var/opt/solr/example/

ENTRYPOINT ["java -jar start.jar"]

#CMD cd /var/opt/solr/example/ && java -jar start.jar &
