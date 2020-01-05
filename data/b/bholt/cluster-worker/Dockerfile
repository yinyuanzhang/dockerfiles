#######################################################
# Base image with my common software and configuration
#######################################################
FROM ubuntu:14.10
MAINTAINER Brandon Holt <holt.bg@gmail.com>

RUN apt-get update && apt-get install -y python-dev python-pip git

RUN git clone https://github.com/sampsyo/cluster-workers.git && \
    cd cluster-workers && \
    python setup.py install

WORKDIR /cluster-workers
ENTRYPOINT ["/usr/bin/env","python"]
