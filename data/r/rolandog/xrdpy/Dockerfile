# XRDPy Docker Image to avoid build times

FROM python:latest

MAINTAINER rolandog@gmail.com

# Runtime Dependencies
RUN apt-get update -qy && apt-get install -y \
    gfortran \
    liblapack-dev \
    liblapack3 \
    python3-dev \
    python3-pip \
    python3-matplotlib \
    python3-numpy \
    python3-progressbar \
    python3-scipy \
 && apt-get upgrade -y \
 && apt-get autoclean -y \
 && apt-get clean -y \
 && apt-get purge -y \
 && apt-get autoremove -y \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf ~/.cache

COPY requirements.txt /tmp/

RUN pip3 install --no-cache-dir -U -r /tmp/requirements.txt