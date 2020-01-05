FROM python:2.7-jessie

# install packages dependencies
RUN apt-get update -yqq && \
    apt-get install -yqq \
        bedtools \
        cmake \
        gcc \
        git \
        make \
        wget && \
    apt-get clean

RUN \
    # Clone and compile freebayes
    cd /opt && \
    git clone --recursive --branch v1.2.0 git://github.com/ekg/freebayes.git && \
    cd freebayes && \
    make && \
    make install && \
    \
    # Install htslib
    cd /tmp && \
    wget "https://github.com/samtools/htslib/releases/download/1.8/htslib-1.8.tar.bz2" && \
    tar -vxjf htslib-1.8.tar.bz2 && \
    cd htslib-1.8 && \
    ./configure --disable-bz2 --disable-lzma && \
    make && \
    make install && \
    rm -rf /tmp/htslib-1.8 && \
    \
    # Install bcftools
    cd /tmp && \
    wget "https://github.com/samtools/bcftools/releases/download/1.9/bcftools-1.9.tar.bz2" && \
    tar -vxjf bcftools-1.9.tar.bz2 && \
    cd bcftools-1.9 && \
    ./configure --disable-bz2 --disable-lzma && \
    make && \
    make install && \
    rm -rf /tmp/bcftools-1.9


ENV PATH $PATH:/opt/freebayes/scripts/:/opt/freebayes/vcflib/scripts/:/opt
WORKDIR /home

# create volumes for MSK users
VOLUME ["/data", "/gpfs", "/ifs"]

ENTRYPOINT [ "freebayes" ]
