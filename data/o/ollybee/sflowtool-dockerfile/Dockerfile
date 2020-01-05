FROM debian:jessie
MAINTAINER oliver.burkill@eukhost.com

EXPOSE 6343/udp

RUN apt-get update\
  && apt-get install -y --no-install-recommends build-essential curl

RUN curl -O http://www.inmon.com/bin/sflowtool-3.22.tar.gz && tar -xvzf sflowtool-3.22.tar.gz
RUN cd sflowtool-3.22 && ./configure && make && make install
RUN apt-get remove --auto-remove --purge -y build-essential curl

ENTRYPOINT ["sflowtool"]
CMD ["--help"]

