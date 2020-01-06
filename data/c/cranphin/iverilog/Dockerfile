FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    autoconf \
    bison \
    flex \
    g++ \
    gcc \
    git \
    gperf \
    make \
&& rm -rf /var/lib/apt/lists/*

RUN git clone --recursive https://github.com/steveicarus/iverilog.git

WORKDIR iverilog

RUN sh autoconf.sh && ./configure && make && make install

CMD [ "/bin/bash" ]
