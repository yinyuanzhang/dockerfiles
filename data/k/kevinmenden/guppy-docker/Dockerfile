FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y wget apt-transport-https
ENV DEBIAN_FRONTEND='noninteractive apt-get install lightdm -y'

# Add ONT repo to system
RUN wget -O- https://mirror.oxfordnanoportal.com/apt/ont-repo.pub |  apt-key add - && \
echo "deb http://mirror.oxfordnanoportal.com/apt xenial-stable non-free" |  tee /etc/apt/sources.list.d/nanoporetech.sources.list
RUN apt-get update

# Install Guppy
RUN apt-get install -y ont-guppy
