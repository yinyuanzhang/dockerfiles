FROM ubuntu:16.04
LABEL maintainer="Steve tsang <mylagimail2004@yahoo.com>"

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get -yq dist-upgrade \
 && apt-get install -yq --no-install-recommends \
    wget \
    locales \
    git \
    build-essential \
    python3-dev \
    python3-pip \
    pigz \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen
RUN pip3 install cutadapt
COPY TruSeq_and_nextera_adapters.consolidated.fa /opt/.
COPY Dockerfile /opt/.

