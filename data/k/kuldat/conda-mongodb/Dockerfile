FROM ubuntu:14.04

MAINTAINER Simone Marzola <simone.marzola@kuldat.com>

RUN locale-gen en_US en_US.UTF-8 && \
    dpkg-reconfigure locales

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" \
    | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list

RUN apt-get update && apt-get install -y \
    build-essential \
    git-core \
    python-dev \
    python-pip \
    wget \
    libpq-dev \
    libxml2-dev \
    libxslt-dev \
    mongodb-org \
    software-properties-common \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /data/db

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget -q http://repo.continuum.io/miniconda/Miniconda-3.7.3-Linux-x86_64.sh && \
    /bin/bash Miniconda-3.7.3-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniconda-3.7.3-Linux-x86_64.sh

ENV PATH /opt/conda/bin:$PATH

RUN conda install pip --yes

ENV LANG C.UTF-8

CMD ["/bin/bash"]
