FROM tensorflow/tensorflow:1.10.1-gpu

# deep learning for genomics, generic image

# generic
RUN apt update -y --fix-missing && \
  apt-get install -y wget git bzip2 screen htop \
  g++ ncurses-dev zlib1g-dev libbz2-dev liblzma-dev
  
# software folder
RUN mkdir -p /software

# samtools
ENV SAMTOOLS_VERSION 1.9

ADD https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2 /tmp/

RUN mkdir /software/samtools-${SAMTOOLS_VERSION} && \
  cd /tmp/ && \
  tar xjvf samtools-${SAMTOOLS_VERSION}.tar.bz2 && \
  cd /tmp/samtools-${SAMTOOLS_VERSION} && \
  ./configure --prefix=/software/samtools-${SAMTOOLS_VERSION} \
  make && \
  make install && \
  echo 'export PATH=/software/samtools-${SAMTOOLS_VERSION}/bin:$PATH' >> ~/.bash_profile && \
  cd

# ucsc tools
RUN mkdir /software/ucsc_tools && \
  rsync -aP rsync://hgdownload.soe.ucsc.edu/genome/admin/exe/linux.x86_64/ /software/ucsc_tools/ && \
  echo 'export PATH=/software/ucsc_tools:$PATH' >> ~/.bash_profile

# bedtools
ENV BEDTOOLS_VERSION 2.27.0

ADD https://github.com/arq5x/bedtools2/releases/download/v${BEDTOOLS_VERSION}/bedtools-${BEDTOOLS_VERSION}.tar.gz /tmp/

RUN mkdir /software/bedtools-${BEDTOOLS_VERSION} && \
  cd /tmp/ && \
  tar -zxvf /tmp/bedtools-${BEDTOOLS_VERSION}.tar.gz && \
  cd /tmp/bedtools2 && \
  make && \
  cp /tmp/bedtools2/bin/* /software/bedtools-${BEDTOOLS_VERSION}/ && \
  echo 'export PATH=/software/bedtools-${BEDTOOLS_VERSION}:$PATH' >> ~/.bash_profile && \
  cd

# source the file to add software to PATH
RUN sed -i '1s:^:. ~/.bash_profile\n:' ~/.bashrc
