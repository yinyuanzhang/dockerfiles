FROM ubuntu:14.04

ENV DEBIAN_FRONTEND    noninteractive
ENV DEBIAN_PRIORITY    critical
ENV DEBCONF_NOWARNINGS yes

RUN apt-get update
RUN apt-get install -y build-essential wget python python-dev bzip2 libbz2-dev gawk libboost-all-dev; \
    apt-get clean all

RUN	wget https://github.com/alekseyzimin/masurca/releases/download/3.2.8/MaSuRCA-3.2.8.tar.gz

RUN tar xvf MaSuRCA-3.2.8.tar.gz && \
	  cd MaSuRCA-3.2.8 && \
	  ./install.sh

ENV	LD_LIBRARY_PATH /MaSuRCA-3.2.8/lib
ENV PATH $PATH:/MaSuRCA-3.2.8/bin

WORKDIR /data
