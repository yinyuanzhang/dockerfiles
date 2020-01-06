FROM debian:8-slim
MAINTAINER Kamer DINC <merkjs@aol.com>

ENV DEBIAN_FRONTEND noninteractive

# setup workdir
RUN mkdir -p /root/work/
WORKDIR /root/work/

# install git
RUN apt-get -y update && apt-get -y install git && apt-get -y install git-ftp

RUN apt-get -y update \
&& apt-get -y install git \
                      git-ftp
RUN apt-get clean \
&& rm -rf /var/lib/apt/lists/* \
          /tmp/* \
          /var/tmp/* \
          /usr/share/man/?? \
          /usr/share/man/??_*
