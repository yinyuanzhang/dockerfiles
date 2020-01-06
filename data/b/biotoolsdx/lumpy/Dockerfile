FROM ubuntu:16.04

MAINTAINER Chen Yuelong <yuelong.chen.btr@gmail.com>

ARG lumpy_version=0.3.0

# Build dependencies
RUN apt-get update && \
        apt-get  install -y \
        apt-transport-https \
        g++ \
        gawk \
        libcurl4-gnutls-dev \
        autoconf \
        libssl-dev \
        git python-dev wget autoconf automake make gcc perl bzip2 \
        zlib1g-dev libbz2-dev \
        liblzma-dev libcurl4-gnutls-dev libncurses5-dev python-pip \
        build-essential \
        libnss-sss \
        curl \
        unzip \
        cmake \
        python \
        bsdmainutils \
        libncursesw5-dev  && \
    cd /tmp/ && \
    wget -c https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2 && \
    tar -jxvf samtools-1.9.tar.bz2 && \
    cd samtools-1.9 && \
    ./configure && make && make install && \
    pip install numpy==1.16.4  scipy==1.2.1 pysam svtyper && \
    cd /tmp/ && \
    wget -c https://github.com/GregoryFaust/samblaster/archive/v.0.1.24.zip && \
    unzip v.0.1.24.zip && \
    cd samblaster-v.0.1.24 && \
    make && cp samblaster /usr/local/bin && \
    cd /tmp/ && \
    wget -c https://github.com/ldc-developers/ldc/releases/download/v0.17.1/ldc2-0.17.1-linux-x86_64.tar.xz && \
    tar xJf ldc2-0.17.1-linux-x86_64.tar.xz && \
    cp ldc2-0.17.1-linux-x86_64/bin/* /usr/local/bin && \
    cp ldc2-0.17.1-linux-x86_64/lib/* /usr/local/lib && \
    wget -c https://github.com/biod/sambamba/releases/download/v0.6.9/sambamba-0.6.9-linux-static.gz && \
    gzip -d sambamba-0.6.9-linux-static.gz && \
    chmod +x sambamba-0.6.9-linux-static && \
    mv sambamba-0.6.9-linux-static /usr/local/bin/sambamba && \
    mkdir -p /opt/softwares/ && \
    cd /opt/softwares/ && \
    wget -c https://github.com/arq5x/lumpy-sv/releases/download/$lumpy_version/lumpy-sv.tar.gz && \
    tar -zxvf lumpy-sv.tar.gz && \
    cd lumpy-sv && \
    make && \
    ln -s /opt/softwares/lumpy-sv/scripts/extractSplitReads_BwaMem \
        /opt/softwares/lumpy-sv/bin/* /usr/local/bin/


RUN rm -rf /tmp/* /opt/softwares/*tar.gz && \
    apt-get clean && \
    apt-get remove -y apt-transport-https \
        g++ \
        autoconf \
        git python-dev wget autoconf automake make gcc   \
         python-pip \
        build-essential \
        curl \
        cmake



CMD bash



