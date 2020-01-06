FROM java:8-jdk

MAINTAINER Bill Lee, lee.minwee@gmail.com

RUN  apt-get update \
  && apt-get install -y wget build-essential gcc-multilib apt-utils zlib1g-dev git \
      libncurses5-dev \
      libncursesw5-dev \
      build-essential \
      zlib1g-dev \
      libbz2-dev \
      liblzma-dev \
      python3 \
      r-base \
      cmake automake autoconf \
      libssl-dev \
      libcurl4-openssl-dev \
  && rm -rf /var/lib/apt/lists/*

# Install ggplot2
RUN echo 'install.packages(c("ggplot2"), repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages.R &&     Rscript /tmp/packages.R

#picard
WORKDIR /opt/picard-tools
RUN wget -O /opt/picard-tools/picard.jar --no-check-certificate https://github.com/broadinstitute/picard/releases/download/2.18.14/picard.jar
COPY picard /opt/picard-tools/
RUN chmod +x /opt/picard-tools/picard

#bwa
WORKDIR /opt/bwa
RUN wget 'https://github.com/lh3/bwa/releases/download/v0.7.15/bwakit-0.7.15_x64-linux.tar.bz2' -O bwakit-0.7.15.tar.bz2 &&   tar xf bwakit-0.7.15.tar.bz2 &&   rm bwakit-0.7.15.tar.bz2 &&   mv bwa.kit/bwa bwa &&   rm -rf bwa.kit

#VerifyBamId
WORKDIR /opt/VerifyBamID
COPY VerifyBamID /opt/VerifyBamID
#RUN cd /tmp/ && git clone https://github.com/statgen/verifyBamID.git && git clone https://github.com/statgen/libStatGen.git
#RUN cd /tmp/libStatGen && git checkout tags/v1.0.14
#RUN cd /tmp/verifyBamID && git checkout tags/v1.1.3 && make
#RUN cp /tmp/verifyBamID/bin/verifyBamID /opt/VerifyBamID
#RUN rm -rf /tmp/verifyBamID /tmp/libStatGen
#RUN cd /opt/ && git clone https://github.com/Griffan/VerifyBamID.git
#RUN cd /opt/VerifyBamID && git checkout tags/1.0.5
#WORKDIR /opt/VerifyBamID
#RUN cmake . && make



#samtools
ENV ZIP=samtools-1.5.tar.bz2
ENV URL=https://github.com/samtools/samtools/releases/download/1.5/
ENV FOLDER=samtools-1.5
ENV DST=/tmp

RUN mkdir /opt/samtools
WORKDIR /opt/samtools
RUN wget $URL/$ZIP -O $DST/$ZIP && \
    tar xvf $DST/$ZIP -C $DST && \
    rm $DST/$ZIP && \
    cd $DST/$FOLDER && \
    make && \
    make prefix=/opt/samtools install && \
    cd / && \
    rm -rf $DST/$FOLDER


ENV PATH="/opt/samtools/bin:/opt/picard-tools:/opt/bwa:/opt/VerifyBamID/bin:${PATH}"
RUN mkdir -p /data
WORKDIR /data

