FROM ubuntu:16.04

MAINTAINER <christoph.hahn@uni-graz.at>

RUN apt-get update && apt-get -y upgrade && apt-get install -y build-essential vim git wget python python3 \
python-dev python-pip python-numpy python-scipy python-biopython \
python3-pip

RUN wget -O- https://mirror.oxfordnanoportal.com/apt/ont-repo.pub | apt-key add - \
echo "deb http://mirror.oxfordnanoportal.com/apt trusty-stable non-free" | tee /etc/apt/sources.list.d/nanoporetech.sources.list && \
apt-get update

#download albacore whl
WORKDIR /usr/src
RUN pip3 install --upgrade pip && wget https://mirror.oxfordnanoportal.com/software/analysis/ont_albacore-2.3.3-cp35-cp35m-manylinux1_x86_64.whl
RUN pip3 install ont_albacore-2.3.3-cp35-cp35m-manylinux1_x86_64.whl

#install porechop
RUN git clone https://github.com/rrwick/Porechop.git && \
cd Porechop && \
python3 setup.py install
#porechop -h

#create working directory and move to entrypoint
VOLUME /home/data
WORKDIR /home/data
