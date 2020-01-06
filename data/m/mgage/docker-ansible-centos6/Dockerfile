FROM centos:centos6 

MAINTAINER Adrian Herrera <aherrera@mgage.com>

# Install yum dependencies
RUN yum -y update && \
    yum install -y \
    gcc \
    libffi-devel \
    python-devel \
    bzip2-devel \
    git \
    openssl \
    openssl-devel \
    sqlite-devel \
    tar

# Install python2.7
RUN cd /tmp && \
    curl https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz -O && \
    tar xvfz Python-2.7.12.tgz && \
    cd Python-2.7.12 && \
    ./configure --prefix=/usr/local && \
    make && \
    make altinstall

# Install setuptools + pip
RUN cd /tmp && \
    curl https://bootstrap.pypa.io/get-pip.py -O &&\
    python2.7 get-pip.py

# Install ansible and its dependencies
RUN pip install ansible==2.1.0 setuptools==11.3.0 boto3 boto virtualenv==13.1.2 credstash==1.11.0 &&\
    yum clean all && rm -rf /tmp/* /var/tmp/*
