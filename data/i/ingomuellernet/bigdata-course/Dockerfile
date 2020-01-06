FROM ubuntu:bionic
MAINTAINER Ingo Müller <ingo.mueller@inf.ethz.ch>

# Basics
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        # For further Docker layers
        python3-pip \
        wget \
        # For the upload script
        curl \
        ghostscript \
        zip \
        # For the large files test
        git \
        git-lfs \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# wkhtmltopdf
RUN cd /tmp/ && \
    wget --progress=dot:giga https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
        apt-get install -y ./wkhtmltox*.deb && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    rm wkhtmltox*.deb

# Jupyter
RUN pip3 install --upgrade \
        jupyter==1.0.0 \
    && rm -r ~/.cache/pip
