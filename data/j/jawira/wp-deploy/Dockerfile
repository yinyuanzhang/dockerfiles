FROM jawira/php

MAINTAINER Jawira Portugal

RUN apt-get update && apt-get install -y \
    git \
    mysql-client-5.7 \
    rsync \
    ssh \
    subversion \
    && apt-get autoremove -y && apt-get autoclean && apt-get clean && rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*
