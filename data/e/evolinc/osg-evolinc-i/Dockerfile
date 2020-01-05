FROM ubuntu:16.04
MAINTAINER Upendra Devisetty
LABEL Description "This Dockerfile is used for OSG-EvolincI"

RUN mkdir /cvmfs /work

RUN apt-get update && apt-get install -y g++ \
		make \
		git \
		zlib1g-dev \
		python \
		perl \
		wget \
		curl \
		python-matplotlib \
		python-numpy \
                python-pandas \
                lsb \
		apt-transport-https \
		python-requests

# Setting the path and working directory
ENV BINPATH /usr/bin
WORKDIR /evolinc_docker

# Install icommands.
RUN wget -qO - https://packages.irods.org/irods-signing-key.asc | apt-key add - \
    && echo "deb [arch=amd64] https://packages.irods.org/apt/ xenial main" > /etc/apt/sources.list.d/renci-irods.list \
    && apt-get update \
    && apt-get install -y irods-icommands

# Cufflinks
RUN wget -O- http://cole-trapnell-lab.github.io/cufflinks/assets/downloads/cufflinks-2.2.1.Linux_x86_64.tar.gz | tar xzvf -

# Transdecoder
RUN wget -O- https://github.com/TransDecoder/TransDecoder/archive/2.0.1.tar.gz | tar xzvf -

# Diamond Blast
RUN wget http://github.com/bbuchfink/diamond/releases/download/v0.9.10/diamond-linux64.tar.gz
RUN tar xzf diamond-linux64.tar.gz

# Samtools
RUN wget --no-check-certificate http://sourceforge.net/projects/samtools/files/samtools/1.0/samtools-bcftools-htslib-1.0_x64-linux.tar.bz2/download
RUN tar xvf download

# Bedtools
RUN wget https://github.com/arq5x/bedtools2/archive/v2.25.0.tar.gz
RUN tar xvf v2.25.0.tar.gz
RUN cd bedtools2-2.25.0 && make
RUN cd ..

# Bedops tool
RUN wget -O- https://github.com/bedops/bedops/releases/download/v2.4.16/bedops_linux_x86_64-v2.4.16.tar.bz2 | tar jxvf -

# cpan
RUN curl -L http://cpanmin.us | perl - App::cpanminus
RUN cpanm URI/Escape.pm

# R libraries
RUN echo "deb http://cran.cnr.berkeley.edu/bin/linux/ubuntu trusty/" >> /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 51716619E084DAB9
RUN apt-get update
RUN apt-get install -y r-base r-base-dev
RUN Rscript -e 'install.packages("splitstackshape", dependencies = TRUE, repos="http://cran.rstudio.com/");'
RUN Rscript -e 'install.packages("dplyr", dependencies = TRUE, repos="http://cran.rstudio.com/");'
RUN Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite("Biostrings");'
RUN Rscript -e 'install.packages("getopt", dependencies = TRUE, repos="http://cran.rstudio.com/");'

# Uniprot database
ADD https://github.com/iPlantCollaborativeOpenSource/docker-builds/releases/download/evolinc-I/uniprot_sprot.dmnd.gz /evolinc_docker/
RUN gzip -d /evolinc_docker/uniprot_sprot.dmnd.gz
RUN chmod 777 /evolinc_docker/uniprot_sprot.dmnd

# rFAM database
ADD https://de.cyverse.org/dl/d/12EF1A2F-B9FC-456D-8CD9-9F87197CACF2/rFAM_sequences.fasta /evolinc_docker/
RUN chmod 755 /evolinc_docker/rFAM_sequences.fasta

# Biopython
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py
RUN pip install biopython

# CPC2 (modified)
ADD CPC2-beta /evolinc_docker/CPC2-beta
WORKDIR /evolinc_docker/CPC2-beta/libs/libsvm/
RUN tar xvf libsvm-3.22.tar.gz
WORKDIR libsvm-3.22
RUN make clean && make
WORKDIR /

#LAST
RUN wget http://last.cbrc.jp/last-926.zip
RUN apt-get install -y unzip
RUN unzip last-926.zip
WORKDIR last-926
RUN make
RUN make install prefix=~

# Evolinc wrapper scripts
ADD *.sh *.py *.R /evolinc_docker/
RUN chmod +x /evolinc_docker/evolinc-part-I.sh && cp /evolinc_docker/evolinc-part-I.sh $BINPATH
WORKDIR /

# Scripts for OSG
ADD upload-files wrapper /usr/bin/

# Environment settings
RUN mkdir /usr/bin/PerlLib

RUN cp /evolinc_docker/cufflinks-2.2.1.Linux_x86_64/cuffcompare $BINPATH && \
    cp /evolinc_docker/cufflinks-2.2.1.Linux_x86_64/cufflinks $BINPATH && \
    cp /evolinc_docker/cufflinks-2.2.1.Linux_x86_64/cuffmerge $BINPATH && \
    cp /evolinc_docker/cufflinks-2.2.1.Linux_x86_64/gffread $BINPATH && \
    cp -r /evolinc_docker/TransDecoder-2.0.1/PerlLib/* $BINPATH/PerlLib && \
    cp -r /evolinc_docker/TransDecoder-2.0.1/util $BINPATH && \
    cp /evolinc_docker/TransDecoder-2.0.1/TransDecoder.LongOrfs $BINPATH && \
    cp /evolinc_docker/bedtools2-2.25.0/bin/bedtools $BINPATH && \
    cp /evolinc_docker/bedtools2-2.25.0/bin/intersectBed $BINPATH && \
    cp /evolinc_docker/bedtools2-2.25.0/bin/sortBed $BINPATH && \
    cp /evolinc_docker/bedtools2-2.25.0/bin/closestBed $BINPATH && \
    cp /evolinc_docker/samtools-bcftools-htslib-1.0_x64-linux/bin/* $BINPATH && \
    cp /evolinc_docker/bin/* $BINPATH && \
    cp /last-926/src/lastal $BINPATH && \
    cp /last-926/src/lastdb $BINPATH && \
    cp /evolinc_docker/diamond $BINPATH 

# Entrypoint
ENTRYPOINT ["evolinc-part-I.sh"]
CMD ["-h"]
