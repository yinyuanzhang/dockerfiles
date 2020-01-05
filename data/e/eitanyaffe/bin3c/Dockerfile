FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y python python-numpy python-dev python-pip git g++

RUN pip install --upgrade pip
RUN pip install 'numpy>=1.13,<1.15.0'

ENV GIT_DIR /git
RUN mkdir $GIT_DIR
RUN cd $GIT_DIR && git clone --recursive https://github.com/cerebis/bin3C.git

WORKDIR $GIT_DIR/bin3C

RUN pip2 install -r requirements.txt

WORKDIR $GIT_DIR
RUN cd $GIT_DIR; git clone https://github.com/mapequation/infomap.git
RUN cd $GIT_DIR/infomap; make; cp Infomap /git/bin3C/external

WORKDIR $GIT_DIR/bin3C
