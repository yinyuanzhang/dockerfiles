############################################################
# Dockerfile to run a Django-based web application
# with nvidia CUDA support
############################################################

# Set the base image to use nvidia cuda
FROM nvidia/cuda:10.0-base

# Set the file maintainer (your name - the file's author)
MAINTAINER Aaron Wong

# Set env variables used in this Dockerfile (add a unique prefix, such as DOCKYARD)
# Local directory with project source
ENV HB_SRC=.
# Directory in container for all project files
ENV HB_SRVHOME=/usr/src/app

# Disable buffering so celery logs print immediately (useful for monitoring but
# can be disabled later). Also allow celery workers to start as root, which is
# normally not allowed.
ENV PYTHONUNBUFFERED=1
ENV C_FORCE_ROOT=1

# Update the default application repository sources list
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y --no-install-recommends \
    python3.7 \
    python3.7-dev \
    python3-pip \
    python3-setuptools \
    build-essential \
    && \
apt-get clean
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1

RUN apt-get install -y \
    mysql-client \
    git-core \
    libcurl4-gnutls-dev libz-dev \
    libblas-dev liblapack-dev gfortran

# Copy application source code to SRCDIR
COPY $HB_SRC $HB_SRVHOME

RUN mkdir $HB_SRVHOME/static
RUN ln -s $HB_SRVHOME/static $HB_SRVHOME/humanbase/static

WORKDIR $HB_SRVHOME

# Needed to boostrap pip3 install -r requirements.txt
RUN pip3 install -r requirements/bootstrap.txt

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Install supervisord
WORKDIR $HB_SRVHOME
COPY supervisord.conf /etc/supervisor/supervisord.conf

WORKDIR $HB_SRVHOME/humanbase
