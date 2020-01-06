FROM biocorecrg/debian-perlbrew-pyenv:stretch

# File Author / Maintainer
MAINTAINER Toni Hermoso Pulido <toni.hermoso@crg.eu> 

ARG DOWNLOAD_URL=http://ekhidna2.biocenter.helsinki.fi/sanspanz/SANSPANZ.3.tar.gz
ARG PROG_DIR=SANSPANZ.3

# Install dependencies
RUN cpanm Switch
RUN pip install requests scipy numpy fastcluster

WORKDIR /usr/local
RUN curl --fail --silent --show-error --location --remote-name ${DOWNLOAD_URL}; tar zxf ${PROG_DIR}.tar.gz; rm ${PROG_DIR}.tar.gz
WORKDIR /usr/local/${PROG_DIR}

# Clean cache
RUN apt-get clean
RUN set -x; rm -rf /var/lib/apt/lists/*

VOLUME /share