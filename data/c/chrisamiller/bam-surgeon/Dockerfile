FROM ubuntu:14.04

WORKDIR /opt/
RUN apt-get update && apt-get install -y software-properties-common

RUN add-apt-repository -y ppa:scipy/ppa

RUN apt-get install -y \
    python \
    python-numpy \
    python-scipy \
    python-pip \
    zlib1g-dev \
    git \
    wget \
    libncurses5-dev \
    libbz2-dev \
    liblzma-dev \
    pkg-config \
    automake \
    autoconf \
    glib-2.0-dev \
    unzip

RUN pip install cython
RUN pip install pysam

RUN wget https://www.ebi.ac.uk/~zerbino/velvet/velvet_1.2.10.tgz
RUN tar xvzf velvet_1.2.10.tgz
RUN make -C velvet_1.2.10
RUN cp velvet_1.2.10/velvetg /usr/bin
RUN cp velvet_1.2.10/velveth /usr/bin

RUN git clone https://github.com/lh3/bwa.git
RUN make -C bwa
RUN cp bwa/bwa /usr/bin

RUN git clone https://github.com/samtools/htslib.git
RUN make -C htslib

RUN git clone https://github.com/samtools/samtools.git
RUN make -C samtools
RUN cp samtools/samtools /usr/bin
RUN cp samtools/misc/wgsim /usr/bin

RUN git clone https://github.com/samtools/bcftools.git
RUN make -C bcftools
RUN cp bcftools/bcftools /usr/bin

RUN wget https://github.com/broadinstitute/picard/releases/download/1.131/picard-tools-1.131.zip
RUN unzip picard-tools-1.131.zip

RUN git clone https://github.com/adamewing/exonerate.git
RUN cd exonerate && autoreconf -fi && ./configure && make && make install

RUN git clone https://github.com/adamewing/bamsurgeon.git
RUN export PATH=$PATH:/usr/bin && cd bamsurgeon && python setup.py install

CMD []
