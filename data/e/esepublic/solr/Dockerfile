FROM debian:jessie
MAINTAINER Keith Bentrup <kbentrup@ebay.com>

RUN apt update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes openjdk-7-jdk \
    solr-tomcat && \
  apt-get --purge autoremove -y && \
  apt-get clean && \
  rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*

RUN chown -R tomcat7:tomcat7 /var/lib/tomcat7 && \
  mkdir /usr/java && \
  ln -s /usr/lib/jvm/java-7-openjdk-amd64 /usr/java/default

EXPOSE 8080
