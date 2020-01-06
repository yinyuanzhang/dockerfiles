FROM ubuntu:18.04 as dev
ENV HOME /root
ENV LD_LIBRARY_PATH /root/affdex-sdk/lib:/usr/local/lib

WORKDIR /root/eplus
COPY ./ubuntu_install.sh ./
RUN sh ubuntu_install.sh

FROM dev as deploy
COPY ./ ./