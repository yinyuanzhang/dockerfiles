FROM sdempsay/docker-java8
MAINTAINER Shawn Dempsay <shawn@dempsay.org>

ENV DEBIAN_FRONTEND noninteractive 
ADD http://apache.mirrors.pair.com/felix/org.apache.felix.main.distribution-4.4.1.tar.gz /tmp/
RUN mkdir -p /opt/felix && cd /opt/felix && tar xzvf /tmp/org.apache.felix.main.distribution-4.4.1.tar.gz
RUN ln -s /opt/felix/felix-framework-4.4.1 /opt/felix/current
CMD cd /opt/felix/current && java -jar bin/felix.jar
