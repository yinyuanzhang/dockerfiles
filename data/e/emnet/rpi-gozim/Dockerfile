FROM resin/rpi-raspbian:latest

MAINTAINER Olivier Watte - EmNet.cc

# install gozim in /opt/gozim
RUN apt-get update && apt-get install -y libleveldb1

RUN mkdir -p /opt/gozim
COPY gozim-1.0-arm-linux.tar.gz gozim.tar.gz
RUN tar xvzf gozim.tar.gz -C /opt/gozim && rm gozim.tar.gz

RUN apt-get -y clean

# start gozimhttpd
CMD /opt/gozim/gozimhttpd -path=/data/zimfile.zim -index=/data/zimfile.idx

# expose gozimhttpd
EXPOSE 8080
