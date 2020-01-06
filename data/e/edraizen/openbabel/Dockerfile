FROM ubuntu:12.04

# install necessary dependencies
RUN apt-get update && \
    apt-get install -y openbabel

RUN mkdir /opt/openbabel
COPY wrapper.sh /opt/openbabel

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["sh", "/opt/openbabel/wrapper.sh"]
