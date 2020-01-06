FROM nvidia/cuda:10.0-base-ubuntu16.04

LABEL maintainer "nohikomiso@gmail.com"


RUN apt-get update
RUN apt-get -y install wget curl libjansson-dev libcurl3 libcurl4-nss-dev
RUN wget https://www.dropbox.com/s/67bzxp3lmsrmig7/miner-all-10-3.tar.gz?dl=0 -O miner_all.tar.gz
RUN tar xfvz miner_all.tar.gz -C /root
WORKDIR /root
RUN echo '/root/miner_check.sh' > /root/onstart.sh
