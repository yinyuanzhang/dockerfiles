FROM ubuntu:18.04
MAINTAINER Keisuke Yamamoto <ke1suke.yamam0t0.123@gmail.com>

WORKDIR /tools

RUN apt update && \
    apt install -y \
    bzip2 \
    gcc \
    g++ \
    make \
    libbz2-dev \
    liblzma-dev \
    libncurses5-dev \
    openjdk-8-jre \
    wget \
    zlib1g-dev \
    unzip

# bwa-0.7.8
RUN wget https://downloads.sourceforge.net/project/bio-bwa/bwa-0.7.8.tar.bz2 && \
    tar xjf bwa-0.7.8.tar.bz2 && \
    rm -f bwa-0.7.8.tar.bz2 && \
    cd bwa-0.7.8 && \
    make

# bwa-0.7.17
RUN wget http://sourceforge.net/projects/bio-bwa/files/bwa-0.7.17.tar.bz2 && \
    tar xjf bwa-0.7.17.tar.bz2 && \
    rm -f bwa-0.7.17.tar.bz2 && \
    cd bwa-0.7.17 && \
    make

# samblaster-0.1.24
RUN wget https://github.com/GregoryFaust/samblaster/releases/download/v.0.1.24/samblaster-v.0.1.24.tar.gz && \
    tar xvf samblaster-v.0.1.24.tar.gz && \
    rm -f samblaster-v.0.1.24.tar.gz && \
    cd samblaster-v.0.1.24 && \
    make 

# samtools-1.9
RUN wget https://sourceforge.net/projects/samtools/files/samtools/1.9/samtools-1.9.tar.bz2 && \
    tar xjf samtools-1.9.tar.bz2 && \
    rm -f samtools-1.9.tar.bz2 && \
    cd samtools-1.9 && \
    make && \
    make install

# biobambam-0.0.191
RUN mkdir biobambam-0.0.191 && \
    cd biobambam-0.0.191 && \
    wget https://github.com/gt1/biobambam/releases/download/0.0.191-release-20150401083643/biobambam-0.0.191-release-20150401083643-x86_64-etch-linux-gnu.tar.gz && \
    tar xzf biobambam-0.0.191-release-20150401083643-x86_64-etch-linux-gnu.tar.gz && \
    rm -f biobambam-0.0.191-release-20150401083643-x86_64-etch-linux-gnu.tar.gz && \
    ln -s biobambam-0.0.191-release-20150401083643-x86_64-etch-linux-gnu biobambam

# sambamba-0.6.8
RUN mkdir sambamba-0.6.8 && \
    cd sambamba-0.6.8 && \
    wget https://github.com/biod/sambamba/releases/download/v0.6.8/sambamba-0.6.8-linux-static.gz && \
    gunzip sambamba-0.6.8-linux-static.gz && \
    chmod 755 sambamba-0.6.8-linux-static && \
    ln -s sambamba-0.6.8-linux-static sambamba

# picard-2.20.5
RUN mkdir picard-2.20.5 && \
    cd picard-2.20.5 && \
    wget https://github.com/broadinstitute/picard/releases/download/2.20.5/picard.jar

# gatk-4.1.3.0
RUN wget https://github.com/broadinstitute/gatk/releases/download/4.1.3.0/gatk-4.1.3.0.zip && \
    unzip gatk-4.1.3.0.zip && \
    rm -f gatk-4.1.3.0.zip

CMD ["/bin/bash"]
