FROM ubuntu:18.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        ca-certificates python3-pip python3-setuptools rpm make file && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/* && \
    ln -s /usr/bin/pip3 /usr/bin/pip && \
    pip install -q virtualenv==16.7.5 Sphinx==1.7.9

ENV VERSION 1

VOLUME [ "/sources", "/output" ]
WORKDIR /sources
CMD [ "deps/bin/run.sh" ]
