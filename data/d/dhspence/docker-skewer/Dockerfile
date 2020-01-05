FROM dhspence/docker-baseimage:latest

# File Author / Maintainer
MAINTAINER David Spencer <dspencer@wustl.edu>

# Install cutadapt 
WORKDIR /opt/

RUN git clone https://github.com/relipmoc/skewer.git && \
    cd skewer && \
    make && \
    cp skewer /usr/local/bin/
