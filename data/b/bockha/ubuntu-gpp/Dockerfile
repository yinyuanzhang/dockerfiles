FROM ubuntu:18.04

LABEL Name buildcontainer

LABEL Version 1.0.0

RUN apt-get update -y \
    && apt-get upgrade -y  \
    && apt-get install -y make g++ zip \
    && apt-get clean

CMD /bin/bash
