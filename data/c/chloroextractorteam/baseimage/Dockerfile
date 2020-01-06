FROM ubuntu:xenial

LABEL maintainer="foersterfrank@gmx.de"

RUN apt update && apt install --yes --no-install-recommends \
    liblog-log4perl-perl \
    libmoose-perl \
    libfile-which-perl \
    libipc-run-perl \
    libterm-progressbar-perl \
    libgraph-perl \
    bowtie2 \
    ncbi-blast+ \
    samtools \
    bedtools \
    r-base \
    ghostscript \
    jellyfish \
    wget \
    build-essential \
    git \
    zlib1g-dev \
    python3-setuptools \
    openjdk-8-jre-headless \
    libncurses5-dev \
    libbz2-dev \
    liblzma-dev \
    python3 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /opt
RUN wget -O spades.tar.gz \
        http://spades.bioinf.spbau.ru/release3.11.1/SPAdes-3.11.1-Linux.tar.gz && \
    tar xvzf spades.tar.gz && \
    rm spades.tar.gz
ENV PATH=/opt/SPAdes-3.11.1-Linux/bin/:"$PATH"

RUN wget https://github.com/samtools/samtools/releases/download/1.4.1/samtools-1.4.1.tar.bz2 && \
    tar xjf samtools-1.4.1.tar.bz2 && \
    cd samtools-1.4.1 && \
    ./configure && \
    make && \
    make check && \
    make install && \
    cd .. && \
    rm -rf samtools-1.4.1 samtools-1.4.1.tar.bz2
