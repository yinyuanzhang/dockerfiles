FROM centos:7

MAINTAINER Krittin Phornsiricharoenphant <oatkrittin@gmail.com>

ENV MOTHUR_HOME         /usr/local/mothur
ENV MOTHUR_VERSION      v.1.41.1
ENV PATH                $MOTHUR_HOME:$PATH

RUN yum update -y && \
    yum install -y unzip wget && \
    yum clean all && \
    rm -rf /var/cache/yum/*

RUN cd /usr/local && \
    wget https://github.com/mothur/mothur/releases/download/${MOTHUR_VERSION}/Mothur.linux_64.zip && \
    unzip Mothur.linux_64.zip && \
    rm -f Mothur.linux_64.zip && \
    rm -rf __MACOSX