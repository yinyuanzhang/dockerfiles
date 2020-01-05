## Dockerfile for dox
## Mac Radigan
##
## Copyright 2016 Mac Radigan
## All Rights Reserved

  FROM ubuntu:latest

  MAINTAINER Mac Radigan

  ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

  ## update APT
  RUN ulimit -n 1024
  RUN apt-get update --fix-missing && \
      apt-get install -y              \
        apt-utils                     \
        pandoc                        \
        gnuplot                       \
        wget                          \
        curl                          \
        build-essential               \
        git                           \
        texlive                       \
        texlive-latex-extra           \
        texlive-science               \
        texlive-full                  \
        python3-pip                   \
        cython3
 
  RUN pip3 install --upgrade pip
 
  RUN python3 -m pip install              pandoc            && \
      python3 -m pip install              sphinx            && \
      python3 -m pip install              sympy             && \
      python3 -m pip install              networkx          && \
      python3 -m pip install              uuid
 
  RUN mkdir -p /opt/dox
  COPY . /opt/dox/

  WORKDIR /opt/dox
  RUN make

  # Dox entry point
  ENTRYPOINT ["/opt/dox/docker/bin/dox_ctl"]

  # clean up APT
  RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

## *EOF*
