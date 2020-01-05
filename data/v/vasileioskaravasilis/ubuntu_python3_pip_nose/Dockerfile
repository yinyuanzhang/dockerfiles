FROM ubuntu:xenial

RUN apt-get -qq update \
&& apt-get -qqy install \
    python3 python3-pip \
&& python3 -m pip install nose \
&& rm -rf /var/lib/apt/lists/*
