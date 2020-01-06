FROM ubuntu:12.04

# install necessary dependencies
RUN apt-get update

WORKDIR /opt
COPY zrank2_linux.tar.gz /opt
RUN tar -xzf zrank2_linux.tar.gz
RUN rm zrank2_linux.tar.gz

COPY wrapper.sh /opt/zrank2_linux

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["sh", "/opt/zrank2_linux/wrapper.sh"]
