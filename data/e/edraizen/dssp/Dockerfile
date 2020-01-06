FROM ubuntu:12.04

# install necessary dependencies
RUN apt-get update && \
    apt-get install -y wget

WORKDIR /opt
RUN mkdir dssp
RUN wget ftp://ftp.cmbi.ru.nl/pub/software/dssp/dssp-2.0.4-linux-i386 -O /opt/dssp/dssp
RUN chmod a+x /opt/dssp/dssp

COPY wrapper.sh /opt/dssp

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["sh", "/opt/dssp/wrapper.sh"]
