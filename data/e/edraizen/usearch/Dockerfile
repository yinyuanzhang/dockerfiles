FROM ubuntu:12.04

# install necessary dependencies
RUN apt-get update && \
    apt-get install -y wget

WORKDIR /opt
RUN mkdir usearch
RUN wget --no-check-certificate https://drive5.com/cgi-bin/upload3.py?license=2018092402493417100 -O /opt/usearch/usearch
RUN chmod a+x /opt/usearch/usearch

COPY wrapper.sh /opt/usearch

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["sh", "/opt/dssp/wrapper.sh"]
