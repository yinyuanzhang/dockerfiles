FROM ubuntu:xenial
ENV VERSION 3.2.2-1

RUN apt-get update && apt-get install -y \
    wget \
    lsb-release \
    procps \
    apt-transport-https
RUN wget -O- https://mirror.oxfordnanoportal.com/apt/ont-repo.pub | apt-key add -
RUN PLATFORM=$(lsb_release -cs) && echo "deb http://mirror.oxfordnanoportal.com/apt ${PLATFORM}-stable non-free" | tee /etc/apt/sources.list.d/nanoporetech.sources.list
RUN apt-get update && apt-get install -y ont-guppy-cpu=$VERSION~xenial

RUN apt-get clean && apt-get purge -y wget lsb-release && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp
