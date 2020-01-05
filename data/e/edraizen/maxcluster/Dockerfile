FROM ubuntu:12.04

# install necessary dependencies
RUN apt-get update && \
    apt-get install -y wget

WORKDIR /opt
RUN mkdir maxcluster
RUN wget http://www.sbg.bio.ic.ac.uk/maxcluster/maxcluster64bit -O /opt/maxcluster/maxcluster
RUN chmod a+x /opt/maxcluster/maxcluster

COPY wrapper.sh /opt/maxcluster

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["sh", "/opt/maxcluster/wrapper.sh"]
