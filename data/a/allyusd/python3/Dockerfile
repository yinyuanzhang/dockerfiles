FROM i386/ubuntu:18.04

RUN apt update && apt install -y python3-pip python3-dev && \
  cd /usr/local/bin && \
  ln -s /usr/bin/python3 python && \
  pip3 install --upgrade pip
