FROM ubuntu:16.04

#install the bareminimum and remove the cache
RUN apt-get update && apt-get install -y --no-install-recommends \
    python \
    python-dev \
    python-numpy \
    python-scipy \
    python-pip \
    python-setuptools \
    python-wheel \
    cython \
    zlib1g-dev \
    libbz2-dev \
    libncurses5-dev \
    liblzma-dev \
    libglib2.0-dev \
    git \
    wget \
    bzip2 \
    pkg-config \
    automake \
    autoconf \
    gcc \
    g++\
    default-jre

ENV VELVET_VERSION 1.2.10
ENV PICARD_VERSION 2.21.2
ENV BWA_VERSION 0.7.17
ENV SAMTOOLS_VERSION 1.9
ENV BCFTOOLS_VERSION 1.9

####################### VELVET #######################
RUN cd /opt \
    && wget https://www.ebi.ac.uk/~zerbino/velvet/velvet_${VELVET_VERSION}.tgz \
    && tar -xvzf velvet_${VELVET_VERSION}.tgz \
    && make -C velvet_${VELVET_VERSION}

ENV PATH=/opt/velvet_${VELVET_VERSION}:$PATH

##################### EXONERATE #####################
RUN cd /opt \
    && git clone https://github.com/adamewing/exonerate.git \
    && cd exonerate \
    && autoreconf -fi \
    && ./configure \
    && make \
    && make install

###################### SAMTOOLS ######################
RUN cd /opt/ \
    && wget https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2 \
    && tar -xjf samtools-${SAMTOOLS_VERSION}.tar.bz2 \
    && rm -f samtools-${SAMTOOLS_VERSION}.tar.bz2 \
    && cd /opt/samtools-${SAMTOOLS_VERSION}/ \
    && make \
    && make install

# ENV PATH="/opt/samtools-${SAMTOOLS_VERSION}/:$PATH"

###################### BCFTOOLS ######################
RUN cd /opt/ \
    && wget https://github.com/samtools/bcftools/releases/download/${BCFTOOLS_VERSION}/bcftools-${BCFTOOLS_VERSION}.tar.bz2 \
    && tar -xjf bcftools-${BCFTOOLS_VERSION}.tar.bz2 \
    && rm -f bcftools-${BCFTOOLS_VERSION}.tar.bz2 \
    && cd /opt/bcftools-${BCFTOOLS_VERSION}/ \
    && make \
    && make install

# ENV PATH="/opt/samtools-${BCFTOOLS_VERSION}/:$PATH"

######################## BWA ########################
RUN cd /opt/ \
    && wget https://github.com/lh3/bwa/releases/download/v${BWA_VERSION}/bwa-${BWA_VERSION}.tar.bz2 \
    && tar -xjf bwa-${BWA_VERSION}.tar.bz2 \
    && rm -f bwa-${BWA_VERSION}.tar.bz2 \
    && cd /opt/bwa-${BWA_VERSION}/ \
    && make

ENV PATH="/opt/bwa-${BWA_VERSION}/:$PATH"

#################### BAMSURGEON ####################
#we really need that version and nothing more, because of backwards compatibility
RUN  pip install pysam==0.12.0

RUN cd /opt \
    && git clone https://github.com/adamewing/bamsurgeon.git \
    && cd bamsurgeon \
    && python setup.py install

###################### PICARD ######################
RUN wget -O /picard.jar https://github.com/broadinstitute/picard/releases/download/${PICARD_VERSION}/picard.jar

ENV BAMSURGEON_PICARD_JAR=/picard.jar


#cleanup
#RUN rm -rf /var/lib/apt/lists/* && apt-get autoremove

CMD []
