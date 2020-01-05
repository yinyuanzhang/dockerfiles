# Pull base image.
FROM ubuntu:16.04

# Install.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y byobu curl git htop man unzip vim wget && \
  apt-get install -y ffmpeg && \
  apt-get install -y python-pip python-dev && \
  pip install --upgrade pip && \
  rm -rf /var/lib/apt/lists/*
  
# Set environment variables.
ENV HOME /root

# Define working directory.
WORKDIR /root

ADD config.json /root/
RUN mkdir /root/src
RUN touch /root/config.json

# Define default command.
CMD ["bash"]

ENTRYPOINT cd /root/src && pip install -r requirements.txt && python start.py && /bin/bash
