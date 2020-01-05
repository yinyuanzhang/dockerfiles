FROM ubuntu:14.04
LABEL maintainer="Pure White" \
    email="daniel48@126.com" \
    company="Dashbase" \
    website="www.dashbase.io"

# Install some essentials and remove cache
RUN \
  apt-get update --fix-missing && \
  apt-get -y upgrade && \
  apt-get install -y python python-pip python-dev git fuse && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/dashbase/dashbase-tools.git && cd dashbase-tools && pip install . && cd .. && rm -rf dashbase-tools
