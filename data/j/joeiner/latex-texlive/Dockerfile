FROM debian:jessie
MAINTAINER Johannes Schreiner "johannes@schreiner.io"

RUN apt-get clean && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get upgrade
RUN apt-get clean && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y texlive-full
RUN mkdir /source
RUN apt-get autoclean && apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

VOLUME ["/source"]
WORKDIR /source
CMD ["bash"]
