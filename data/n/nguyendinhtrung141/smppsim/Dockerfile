FROM docker.io/anapsix/alpine-java
MAINTAINER Trung Nguyen Dinh <nguyendinhtrung141@gmail.com>

RUN mkdir -p /opt/local
WORKDIR /opt/local

RUN wget http://www.seleniumsoftware.com/downloads/SMPPSim.tar.gz && tar -xzf SMPPSim.tar.gz

WORKDIR /opt/local/SMPPSim
RUN chmod +x startsmppsim.sh

CMD /opt/local/SMPPSim/startsmppsim.sh
