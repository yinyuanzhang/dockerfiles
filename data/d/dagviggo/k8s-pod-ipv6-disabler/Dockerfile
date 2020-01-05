FROM ubuntu:18.10

RUN apt-get update
RUN apt-get install -y net-tools iproute2

ADD disable.sh /
RUN chmod a+x /disable.sh

ENTRYPOINT /disable.sh