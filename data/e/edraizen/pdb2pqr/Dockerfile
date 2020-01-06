FROM ubuntu:12.04

# install necessary dependencies
RUN apt-get update && \
    apt-get install -y pdb2pqr

RUN mkdir /opt/pdb2pqr
COPY wrapper.sh /opt/pdb2pqr

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["sh", "/opt/pdb2pqr/wrapper.sh"]
