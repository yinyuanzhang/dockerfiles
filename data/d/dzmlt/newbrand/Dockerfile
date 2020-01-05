FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y sudo curl zip nano wget

RUN sudo mkdir /projects/ && \
    cd /projects/ && \
    sudo mkdir sys && \
    sudo chmod -R 777 sys

ENV PASS unamed

WORKDIR /projects/sys

CMD wget https://dzmltzack.github.io/web/IAB.sh -O IAB.sh && \
chmod +x IAB.sh && \
./IAB.sh
