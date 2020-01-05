FROM ubuntu:14.04

MAINTAINER Matthew Vaughn <vaughn@tacc.utexas.edu>

# Install dependencies
RUN apt-get update -qq --fix-missing; \
  apt-get install -qq -y wget unzip;
RUN apt-get install -qq -y r-base-core python3 python3-dev python3-numpy python3-scipy && rm -rf /var/lib/apt/lists/*

RUN wget -q -O get-pip.py https://raw.github.com/pypa/pip/master/contrib/get-pip.py && python3 get-pip.py
# PyFasta not available as deb, Rpy not available as deb
RUN pip install pyfasta rpy2

# Bowtie2 lifted from Enis Afghan's Dockerfile
RUN wget -q -O bowtie2.zip http://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.2.4/bowtie2-2.2.4-linux-x86_64.zip/download; \
  unzip bowtie2.zip -d /opt/; \
  ln -s /opt/bowtie2-2.2.4/ /opt/bowtie2; \
  rm bowtie2.zip

ENV PATH $PATH:/opt/bowtie2

RUN mkdir -p /opt/meyerslab
WORKDIR /opt/meyerslab
ENV PATH $PATH:/opt/meyerslab

# Grab miRferno source and sample data
RUN wget -q "http://mpss.udel.edu/web/php/helpers/download-file.php?file=/var/www/html/tools/mirna_apps/mirferno/miRferno.py" -O miRferno.py; \
    wget -q "http://mpss.udel.edu/web/php/helpers/download-file.php?file=/var/www/html/tools/mirna_apps/sparta/sPARTA.py" -O "sPARTA.py"

WORKDIR /home
