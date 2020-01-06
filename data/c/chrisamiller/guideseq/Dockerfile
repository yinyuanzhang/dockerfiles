#FROM ubuntu:18.10
FROM python:2.7.15-stretch
MAINTAINER Chris Miller <c.a.miller@wustl.edu>

LABEL Image for github.com/aryeelab/guideseq

#some basic tools
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    build-essential \
    bzip2 \
    ca-certificates \
    curl \
    git \
    grep \
    less \
    libcurl4-openssl-dev \
    libpng-dev \
    libssl-dev \
    libxml2-dev \
    make \
    openssh-client \
    unzip \
    wget \
    zip \
    zlib1g-dev

##############
## bedtools ##

WORKDIR /usr/local
RUN git clone https://github.com/arq5x/bedtools2.git && \
    cd /usr/local/bedtools2 && \
    git checkout v2.25.0 && \
    make && \
    ln -s /usr/local/bedtools2/bin/* /usr/local/bin/

# ##############
# ##guideseq
# #RUN cd /opt/ && wget --no-check-certificate https://github.com/aryeelab/guideseq/archive/1.1b5.tar.gz && \
# #    tar -xzvf 1.1b5.tar.gz && \ 
RUN cd /opt && \
    git clone https://github.com/chrisamiller/guideseq.git && \
    cd /opt/guideseq/ && \
    pip install numpy && \
    pip install -r requirements.txt
#     pip install --upgrade pip==9.0.3 && \
#     pip install setuptools && \
#     pip install numpy==1.14.1 && \
#     pip install HTSeq==0.6.1p1 && \
#     pip install PyYAML==3.11 && \
#     pip install swalign==0.3.1 && \
#     pip install nwalign==0.3.1 && \
#     pip install pyfaidx==0.2.7 && \
#     pip install svgwrite==1.1.6 && \
#     pip install regex



#     # pip install -r requirements.txt
# #pip install --upgrade pip 

# #################################
# # Python 2 and 3, plus packages

# # Install Python 2
# # dependencies sometimes get weird - installing each on it's own line seems to help
# # RUN conda create --quiet --yes -p $CONDA_DIR/envs/python2 python=2.7 'pip' && \
# #     conda clean -tipsy && \
# #     /bin/bash -c "source activate python2 && \
# # RUN pip install HTSeq==0.6.1p1 && \
# #     pip install PyYAML==3.11 && \
# #     pip install swalign==0.3.1 && \
# #     pip install nwalign==0.3.1 && \
# #     pip install pyfaidx==0.2.7 && \
# #     pip install svgwrite==1.1.6 && \
# #     pip install regex && \
# #     pip install numpy==1.14.1
# # #    source deactivate"

   
# needed for MGI data mounts
RUN apt-get update && apt-get install -y libnss-sss && apt-get clean all

#set timezone to CDT
#LSF: Java bug that need to change the /etc/timezone.
#/etc/localtime is not enough.
RUN ln -sf /usr/share/zoneinfo/America/Chicago /etc/localtime && \
    echo "America/Chicago" > /etc/timezone && \
    dpkg-reconfigure --frontend noninteractive tzdata

#UUID is needed to be set for some applications
RUN apt-get update && apt-get install -y dbus && apt-get clean all
RUN dbus-uuidgen >/etc/machine-id
