FROM ubuntu:12.04

# install necessary dependencies
RUN apt-get update && \
    apt-get install -y wget

WORKDIR /opt
COPY scwrl4.tgz /opt
RUN tar -xzf scwrl4.tgz
RUN rm scwrl4.tgz

COPY wrapper.sh /opt/scwrl4

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["sh", "/opt/scwrl4/wrapper.sh"]
