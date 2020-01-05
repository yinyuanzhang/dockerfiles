FROM ubuntu
MAINTAINER me

VOLUME  [ "/dumps" ]
RUN apt-get -y update &&  apt-get -y -q install tcpdump

ENTRYPOINT [ "/usr/sbin/tcpdump" ]

