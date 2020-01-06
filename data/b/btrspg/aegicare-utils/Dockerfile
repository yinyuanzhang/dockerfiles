FROM python:3.5.7-slim-stretch

MAINTAINER CHEN, Yuelong <yuelong.chen.btr@gmail.com>
ARG github_token
RUN apt update -y \
    && apt install -y git gcc make zlib1g-dev libbz2-dev liblzma-dev

WORKDIR /tmp/
ADD . /tmp/
RUN pip3 install git+https://$github_token@github.com/btrspg/Aegicare-bioinfo-lib.git \
    && pip3 install -r requirements.txt \
    && python3 setup.py install

RUN apt-get clean && \
    apt-get remove --yes --purge  git gcc make && \
    rm -rf /tmp/*

CMD python