FROM ubuntu:12.04

# install necessary dependencies
RUN apt-get update && \
    apt-get install -y wget bzip2

WORKDIR /opt
RUN mkdir MMalign
WORKDIR /opt/MMalign
RUN wget --no-check-certificate https://zhanglab.ccmb.med.umich.edu/MM-align/MMalign.tar.bz2
RUN tar -jxvf /opt/MMalign/MMalign.tar.bz2
RUN rm /opt/MMalign/MMalign.tar.bz2

COPY wrapper.sh /opt/MMalign

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["sh", "/opt/MMalign/wrapper.sh"]
