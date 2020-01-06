FROM ubuntu:16.04

SHELL ["/bin/bash", "-c"]

# Set locale
RUN apt-get update && apt-get install -y locales && locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:ubuntugis/ubuntugis-unstable && \
    apt-get update && \
    #apt-get install -y libtcmalloc-minimal4 && \
    apt-get install -y grass grass-dev python python-pip && \
    apt-get install -y tar && \
    pip install biopython geojson ete2 pyshp && \
    pip install pandas==0.19.2

##per migliorare gestione memoria 
#ENV LD_PRELOAD /usr/lib/libtcmalloc_minimal.so.4
