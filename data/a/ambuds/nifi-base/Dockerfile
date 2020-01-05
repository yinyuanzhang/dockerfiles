from java:8
RUN mkdir -p /opt/nifi
RUN apt-get -y update
RUN apt-get -y install wget
RUN wget http://mirrors.ocf.berkeley.edu/apache/nifi/0.6.1/nifi-0.6.1-bin.tar.gz -O /tmp/nifi.tar.gz
RUN tar xf /tmp/nifi.tar.gz -C /opt/nifi/
RUN rm -rf /tmp/nifi.tar.gz
