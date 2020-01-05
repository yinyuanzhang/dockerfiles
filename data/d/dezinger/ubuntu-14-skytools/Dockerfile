FROM dezinger/ubuntu-14:latest

MAINTAINER dezinger@gmail.com

ENV DEBIAN_FRONTEND noninteractive

COPY files/ /

RUN \
    apt-get -y update && apt-get install --no-install-recommends -y \ 
# Install
    skytools && \
# clean
    apt-get -y autoremove && apt-get -y clean && apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*