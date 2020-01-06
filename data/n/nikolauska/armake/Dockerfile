FROM ubuntu:18.04

RUN apt-get -y update && \
    apt-get -y install software-properties-common && \
    add-apt-repository ppa:koffeinflummi/armake && \
    apt-get -y update && \
    apt-get -y install armake make
