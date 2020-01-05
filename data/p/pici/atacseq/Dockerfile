FROM ubuntu:16.04
MAINTAINER Danny Wells "danny@parkerici.org"


RUN apt-get update \
    && apt-get install -y git libpng-dev libssl-dev openssl libmysqld-dev make gcc g++ build-essential wget vim

RUN git clone https://github.com/ENCODE-DCC/kentUtils.git \
    && cd /kentUtils \
    && make

RUN wget http://bejerano.stanford.edu/resources/greatTools.tar.gz \
    && tar xzvf greatTools.tar.gz

COPY makefile /greatTools
ENV LD_LIBRARY_PATH usr/lib:/usr/local/lib

RUN cd /greatTools \
    && make 

RUN apt-get update \
    && apt-get install -y software-properties-common wget \
    && add-apt-repository ppa:openjdk-r/ppa \
    && apt-get install -y python python3-pip wget curl unzip python-dev python-setuptools emacs less lynx hdfview zlib1g-dev libncurses5-dev libncursesw5-dev cmake tar gawk valgrind sed build-essential hdf5-tools libhdf5-dev hdf5-helpers libhdf5-serial-dev apt-utils python-pip tabix r-base r-base-dev unzip


#Install samtools
RUN	wget https://sourceforge.net/projects/samtools/files/samtools/1.1/samtools-1.1.tar.bz2/download \
	  && bunzip2 download \
	  && tar -xvf download.out \
	  # && rm download \
	  # && rm -r download.out \
	  && cd samtools-1.1 \
	  && make 

RUN wget https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.1.0/bowtie2-2.1.0-linux-x86_64.zip/download \
	&& unzip download 

RUN wget https://github.com/broadinstitute/picard/releases/download/1.141/picard-tools-1.141.zip  \
	&& unzip picard-tools-1.141.zip

RUN wget http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.5.zip \
	  && unzip fastqc_v0.11.5.zip \
	  && cd FastQC/ \
	  && chmod 755 fastqc 


RUN apt-get install bedtools

RUN wget http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/wigToBigWig \ 
	&& mkdir ucsc_genometools \ 
	&& chmod 755 wigToBigWig \ 
	&& mv wigToBigWig /ucsc_genometools/ 

RUN apt-get install -y python-numpy 

RUN pip install MACS2
RUN apt-get install -y sudo

RUN cd / && rm *.gz *.zip *.out

RUN wget https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs920/ghostscript-9.20.tar.gz && \
	tar zxvf ghostscript-9.20.tar.gz && \
	cd ghostscript-9.20 && \
	./configure && \
	make && \
	sudo make install
	
RUN 	mkdir homer && \
	cd homer && \
	wget http://homer.salk.edu/homer/configureHomer.pl && \
	perl /homer/configureHomer.pl -install && \
	perl /homer/configureHomer.pl -install hg19  && \ 
	perl /homer/configureHomer.pl -install mm8 




ENV PICARD_JAR="/picard-tools-1.141/picard.jar"
ENV PATH="/samtools-1.1:/bowtie2-2.1.0:/FastQC:/picard-tools-1.141:/ucsc_genometools:/homer/bin:${PATH}"



