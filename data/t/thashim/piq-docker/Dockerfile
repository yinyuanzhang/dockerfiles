FROM thashim/basic-docker

MAINTAINER Tatsunori Hashimoto <thashim@mit.edu>


USER root

#update R
RUN sudo echo 'deb http://cran.rstudio.com/bin/linux/ubuntu trusty/' >> /etc/apt/sources.list
RUN gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9
RUN gpg -a --export E084DAB9 | sudo apt-key add -
RUN sudo apt-get update
RUN sudo apt-get install -q -y r-base r-base-dev r-recommended

RUN mkdir /basepiq-tmp
RUN mkdir /scratch/
RUN mkdir /scratch/tmp
RUN mkdir /scratch/data
RUN git clone https://thashim@bitbucket.org/thashim/piq-single.git /basepiq-tmp
RUN Rscript /basepiq-tmp/common.global.r
RUN echo 'source("http://www.bioconductor.org/biocLite.R");biocLite("BSgenome.Hsapiens.UCSC.hg19.masked");biocLite("BSgenome.Mmusculus.UCSC.mm10.masked")' | R --vanilla

#docker build -t=thashim/piq .
#docker run -u $(id -u) -v /cluster/:/cluster/ -w /cluster/thashim/basepiq/ -i thashim/piq /cluster/thashim/basepiq/bam2rdata.r /cluster/thashim/basepiq/common.r /cluster/thashim/PIQ/bams/k562rep1.RData /cluster/projects/wordfinder/bams/wgEncodeOpenChromDnaseK562AlnRep1V2.bam
