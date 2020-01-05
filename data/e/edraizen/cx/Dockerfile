FROM ubuntu:12.04

# install necessary dependencies
RUN apt-get update && \
    apt-get install -y build-essential wget

WORKDIR /opt
RUN mkdir cx
RUN wget ftp://ftp.icgeb.trieste.it/pub/CX/CX.c.gz -O /opt/cx/CX.c.gz
RUN gunzip /opt/cx/CX.c.gz
RUN gcc -o /opt/cx/cx /opt/cx/CX.c -lm
RUN rm /opt/cx/CX.c

COPY wrapper.sh /opt/cx

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["sh", "/opt/cx/wrapper.sh"]
