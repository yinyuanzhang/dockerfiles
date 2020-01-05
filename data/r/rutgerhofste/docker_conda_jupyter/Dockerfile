FROM nvidia/cuda:9.0-runtime-ubuntu16.04
MAINTAINER Rutger Hofste <rutger.hofste@wri.org>

RUN apt-get update && apt-get install -y \
  git \
  wget \
  bzip2 \
  unzip \
  gcc

RUN wget https://repo.continuum.io/archive/Anaconda3-4.4.0-Linux-x86_64.sh 
RUN bash Anaconda3-4.4.0-Linux-x86_64.sh -b -p /opt/anaconda3

ENV PATH /opt/anaconda3/bin:$PATH

VOLUME /volumes/data

# setup folder structure for config file and keys for SSL
RUN mkdir /root/.jupyter
RUN mkdir /.keys
RUN chmod 400 /.keys
RUN mkdir -p /volumes/repos

RUN conda install nb_conda -y

RUN jupyter nbextension enable --py --sys-prefix widgetsnbextension

# currently not used. Additional port
EXPOSE 8000

# Jupyter notebook / lab standard port web traffic
EXPOSE 8888

# Visdom standard port
EXPOSE 8097



