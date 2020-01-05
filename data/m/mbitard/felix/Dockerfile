FROM ubuntu:precise
MAINTAINER Michaël Bitard <bitard.michael [at] gmail [dot] com>

# Install dependencies
RUN apt-get -y update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes software-properties-common python-software-properties
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt-get -y update
RUN /bin/echo debconf shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install oracle-java8-installer oracle-java8-set-default

ADD http://apache.crihan.fr/dist//felix/org.apache.felix.main.distribution-4.4.1.tar.gz /root/felix.tgz
RUN tar xvzf /root/felix.tgz -C /root/

CMD cd /root/felix-framework-4.4.1 && java -jar bin/felix.jar
