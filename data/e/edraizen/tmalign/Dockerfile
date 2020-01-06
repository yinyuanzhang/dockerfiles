FROM ubuntu:12.04

# install necessary dependencies
RUN apt-get update && \
    apt-get install -y wget gfortran

WORKDIR /opt
RUN mkdir TMalign
WORKDIR /opt/TMalign
RUN wget --no-check-certificate https://zhanglab.ccmb.med.umich.edu/TM-align/TMalign.f
RUN gfortran -static -O3 -ffast-math -lm -o TMalign TMalign.f
RUN rm TMalign.f

COPY wrapper.sh /opt/TMalign

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["sh", "/opt/TMalign/wrapper.sh"]
