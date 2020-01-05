FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y python python-numpy python-dev python-pip git g++

ENV GIT_DIR /git
RUN mkdir $GIT_DIR
RUN cd $GIT_DIR && git clone https://github.com/cerebis/sim3C.git

WORKDIR $GIT_DIR/sim3C

# install python packages
RUN pip install -U -r requirements.txt
