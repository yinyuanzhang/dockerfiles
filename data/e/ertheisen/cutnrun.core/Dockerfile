FROM ubuntu:bionic

#Adapted from https://github.com/openanalytics/r-base/blob/master/Dockerfile
#Updated for ubuntu bionic

## Add user to 'staff' group, granting them write privileges to /usr/local/lib/R/site.library
RUN useradd docker \
	&& mkdir /home/docker \
	&& chown docker:docker /home/docker \
	&& addgroup docker staff

RUN apt-get update \ 
	&& apt-get install -y gnupg2 software-properties-common \
    && apt-key adv --keyserver keyserver.ubuntu.com \
        --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 \
    && add-apt-repository \
        'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/' \
    && apt-get update \ 
    && apt-get install -y --no-install-recommends \
		git \
        ed \
		less \
		locales \
		vim-tiny \
		wget \
		ca-certificates \
		apt-transport-https \
		gsfonts \
        libssl-dev \
        libcurl4-openssl-dev \
        libxml2-dev \
        libudunits2-dev \
        libnetcdf-dev \
        python3-pip \
        python3-setuptools \
        python3-dev \        
	&& rm -rf /var/lib/apt/lists/*

## Configure default locale, see https://github.com/rocker-org/rocker/issues/19
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
	&& locale-gen en_US.utf8 \
	&& /usr/sbin/update-locale LANG=en_US.UTF-8

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8

ENV R_BASE_VERSION 3.5.1-1bionic
ENV DEBIAN_FRONTEND=noninteractive
## Now install R and littler, and create a link for littler in /usr/local/bin
## Also set a default CRAN repo, and make sure littler knows about it too
RUN echo "r-base Geographic area: select 12" | debconf-set-selections \
    && apt-get update \
	&& apt-get install -y --no-install-recommends \
		littler\
        r-cran-littler \
		r-base=${R_BASE_VERSION}* \
		r-base-dev=${R_BASE_VERSION}* \
		r-recommended=${R_BASE_VERSION}* \
        && echo 'options(repos = c(CRAN = "https://cloud.r-project.org/"), download.file.method = "libcurl")' >> /etc/R/Rprofile.site \
        && echo 'source("/etc/R/Rprofile.site")' >> /etc/littler.r \
	&& ln -s /usr/share/doc/littler/examples/install.r /usr/local/bin/install.r \
	&& ln -s /usr/share/doc/littler/examples/install2.r /usr/local/bin/install2.r \
	&& ln -s /usr/share/doc/littler/examples/installGithub.r /usr/local/bin/installGithub.r \
	&& ln -s /usr/share/doc/littler/examples/testInstalled.r /usr/local/bin/testInstalled.r \
	&& install.r docopt \
	&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /build

#Install Bioconductor Core Packages
COPY bioconductor_core.R /build/bioconductor_core.R
RUN Rscript bioconductor_core.R 

#Install Python3 Core Packages
COPY requirements_core.txt /build/requirements_core.txt
RUN pip3 install wheel \
    && pip3 install -r requirements_core.txt

#Install iRkernel
COPY iRkernel.R /build/iRkernel.R 
RUN  Rscript iRkernel.R


RUN apt-get update && apt-get install -y \
	curl \
	unzip \
	perl \
	openjdk-8-jre-headless

# Installs fastqc from compiled java distribution into /opt/FastQC
ENV DEST_DIR /opt/

ENV FASTQC_URL http://www.bioinformatics.babraham.ac.uk/projects/fastqc/
ENV FASTQC_VERSION 0.11.4
ENV FASTQC_RELEASE fastqc_v${FASTQC_VERSION}.zip


# Make destination directory
RUN mkdir -p $DEST_DIR

# Download & extract archive - Repo includes binaries for linux
WORKDIR /tmp

# Do this in one command to avoid caching the zip file and its removal in separate layers
RUN curl -SLO ${FASTQC_URL}/${FASTQC_RELEASE} && unzip ${FASTQC_RELEASE} -d ${DEST_DIR} && rm ${FASTQC_RELEASE}

# Make the wrapper script executable
RUN chmod a+x ${DEST_DIR}/FastQC/fastqc

# Include it in PATH
ENV PATH ${DEST_DIR}/FastQC:$PATH



ENV SAMTOOLS_URL https://github.com/samtools/samtools/releases/download/1.9/
ENV SAMTOOLS_VERSION 1.9
ENV SAMTOOLS_RELEASE samtools-${SAMTOOLS_VERSION}.tar.bz2

RUN mkdir -p ${DEST_DIR}/samtools-${SAMTOOLS_VERSION}

WORKDIR /tmp

# Do this in one command to avoid caching the zip file and its removal in separate layers
RUN curl -SLO ${SAMTOOLS_URL}/${SAMTOOLS_RELEASE} && tar xjvf samtools-${SAMTOOLS_VERSION}.tar.bz2
RUN cd samtools-${SAMTOOLS_VERSION}   \
	&& ./configure --prefix=${DEST_DIR}/samtools-${SAMTOOLS_VERSION} \
	&& make install

# Make the wrapper script executable
RUN chmod a+x ${DEST_DIR}/samtools-${SAMTOOLS_VERSION}/bin

# Include it in PATH
ENV PATH ${DEST_DIR}/samtools-${SAMTOOLS_VERSION}/bin:$PATH

RUN pip3 install cutadapt


ENV TRIMGALORE_URL https://github.com/FelixKrueger/TrimGalore/archive/
ENV TRIMGALORE_VERSION 0.4.5
ENV TRIMGALORE_RELEASE trim_galore-${TRIMGALORE_VERSION}.tar.gz

RUN mkdir -p ${DEST_DIR}/trim_galore-${TRIMGALORE_VERSION}

WORKDIR /tmp
RUN curl -fsSL https://github.com/FelixKrueger/TrimGalore/archive/0.4.5.tar.gz -o ${TRIMGALORE_RELEASE} \
	&& tar xvzf ${TRIMGALORE_RELEASE} \
	&& mv TrimGalore-${TRIMGALORE_VERSION}/trim_galore ${DEST_DIR}/trim_galore-${TRIMGALORE_VERSION}

# Make the wrapper script executable
RUN chmod a+x ${DEST_DIR}/trim_galore-${TRIMGALORE_VERSION}

# Include it in PATH
ENV PATH ${DEST_DIR}/trim_galore-${TRIMGALORE_VERSION}:$PATH

RUN ls -la /opt/*/bin/

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python-minimal \
        python-pip \
        python-setuptools \
        python-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install numpy
RUN pip install wheel
RUN pip install macs2

## Install bowtie2
WORKDIR /tmp

ENV BOWTIE2_URL https://sourceforge.net/projects/bowtie-bio/files/bowtie2
ENV BOWTIE2_VERSION 2.3.4.3
ENV BOWTIE2_RELEASE bowtie2-${BOWTIE2_VERSION}.tar.gz


## Install bowtie2
RUN wget ${BOWTIE2_URL}/${BOWTIE2_VERSION}/bowtie2-${BOWTIE2_VERSION}-linux-x86_64.zip/download \
	&& unzip download \
    && rm download \
	&& mv bowtie2-${BOWTIE2_VERSION}-linux-x86_64 ${DEST_DIR}/bowtie2-${BOWTIE2_VERSION} 

ENV PATH ${DEST_DIR}/bowtie2-${BOWTIE2_VERSION}:$PATH

#Install UCSC programs
RUN apt-get update \
    && apt-get install -y openssh-server openssh-client rsync grsync

RUN mkdir -p ${DEST_DIR}/UCSC-utils
WORKDIR ${DEST_DIR}/UCSC-utils
RUN rsync -aP rsync://hgdownload.soe.ucsc.edu/genome/admin/exe/linux.x86_64/ ./

ENV PATH ${DEST_DIR}/UCSC-utils:$PATH
ENV PATH ${DEST_DIR}/UCSC-utils/blat:$PATH

WORKDIR /tmp

## Install Enriched Domain Detector
RUN pip install pysam==0.11.2.2
RUN pip install cython
RUN pip install edd

## Install deeptools
RUN pip3 install py2bit
RUN pip3 install pyBigWig
RUN pip3 install deeptools

RUN mkdir -p /appscripts
RUN sed -i -e "/^assistive_technologies=/s/^/#/" /etc/java-8-openjdk/accessibility.properties

RUN pip install matplotlib \
	&& pip install scipy \
	&& pip install pybedtools \
	&& pip install pysam \
	&& pip install pandas

RUN apt-get install python-tk -y

##Install STAR
ENV STAR_URL https://github.com/alexdobin/STAR/archive/
ENV STAR_VERSION 2.6.1d
ENV STAR_RELEASE ${STAR_VERSION}.tar.gz

RUN mkdir -p ${DEST_DIR}/STAR-${STAR_VERSION}

WORKDIR /tmp

# Do this in one command to avoid caching the zip file and its removal in separate layers
RUN curl -SLO ${STAR_URL}/${STAR_RELEASE} && tar -xzf ${STAR_VERSION}.tar.gz
RUN mv STAR-${STAR_VERSION}/ ${DEST_DIR}

# Make the wrapper script executable
RUN chmod a+x ${DEST_DIR}/STAR-${STAR_VERSION}/bin

# Include it in PATH
ENV PATH ${DEST_DIR}/STAR-${STAR_VERSION}/bin/Linux_x86_64_static:$PATH

RUN apt-get install bedtools

