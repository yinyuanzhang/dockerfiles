FROM merckey/hotpot:centos-7 
##############################################################
# Dockerfile Version:   0.1
# Software: 		bwa + samtools         
# Software Version:     
# Software Website:   
# Description:         
##############################################################

ENV BWA=0.7.17
ENV SAMTOOLS=1.9

RUN yum install -y bzip2-devel \
                   ncurses-devel \
                   xz-devel \
                   zlib-devel ; \
    yum clean all
WORKDIR /tmp/

RUN curl -L -o htslib-$SAMTOOLS.tar.gz https://github.com/samtools/htslib/archive/$SAMTOOLS.tar.gz ; \
    curl -L -o samtools-$SAMTOOLS.tar.gz https://github.com/samtools/samtools/archive/$SAMTOOLS.tar.gz ; \
    curl -L -o bcftools-$SAMTOOLS.tar.gz https://github.com/samtools/bcftools/archive/$SAMTOOLS.tar.gz ; \
    tar xzf bcftools-$SAMTOOLS.tar.gz ; \
    tar xzf htslib-$SAMTOOLS.tar.gz ; \
    tar xzf samtools-$SAMTOOLS.tar.gz ; \
    mv htslib-$SAMTOOLS htslib ; \
    cd htslib && make && make install && cd .. ; \
    cd bcftools-$SAMTOOLS && make -j HTSDIR=../htslib && make install && cd .. ; \
    cd samtools-$SAMTOOLS && make -j HTSDIR=../htslib && make install && cd .. 
RUN curl -L -o bwa-$BWA.tar.gz https://github.com/lh3/bwa/archive/v$BWA.tar.gz ; \
    tar xzf bwa-$BWA.tar.gz ; \
    cd bwa-$BWA && make && cp bwa /usr/bin/bwa ; \
    rm -rf /tmp/*
CMD ["/bin/bash"]
