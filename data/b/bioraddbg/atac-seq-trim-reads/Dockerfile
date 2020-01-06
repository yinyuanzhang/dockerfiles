FROM ubuntu:16.04

MAINTAINER Bio-Rad Support <support@bio-rad.com>

# fastqc requires java
RUN apt-get update && apt-get install -y \
  curl \
  unzip \
  perl \
  openjdk-8-jre-headless \
  python3-pip

# TRIMMOMATIC
ENV TRIMMO_URL http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/
ENV TRIMMO_VERSION 0.38
ENV TRIMMO_RELEASE Trimmomatic-${TRIMMO_VERSION}.zip
ENV DEST_DIR /opt/

# Make destination directory
RUN mkdir -p $DEST_DIR

# Make data directory
RUN mkdir -p /data/

# Download & extract archive - Repo includes binaries for linux
WORKDIR /data/

# Do this in one command to avoid caching the zip file and its removal in separate layers
RUN curl -SLO ${TRIMMO_URL}/${TRIMMO_RELEASE} && unzip ${TRIMMO_RELEASE} -d ${DEST_DIR} && rm ${TRIMMO_RELEASE}

# Add script to run read trimming
COPY src/run_read_trimmer.sh /run_read_trimmer.sh

# CUTADAPT
RUN pip3 install --user --upgrade cutadapt
RUN curl -fsSL https://github.com/FelixKrueger/TrimGalore/archive/0.4.5.tar.gz -o trim_galore.tar.gz
RUN tar xvzf trim_galore.tar.gz
RUN mv TrimGalore-0.4.5 /opt/
RUN ln -s ~/.local/bin/cutadapt /usr/bin/

# Add license
COPY LICENSE.txt /LICENSE.txt

# Pull in some ARGS for defining container name
ARG IMAGE_NAME
ARG SOURCE_BRANCH
ARG SOURCE_COMMIT
RUN printf "Container Name: $IMAGE_NAME\n" > imageInfo.txt
RUN printf "Source Branch: $SOURCE_BRANCH\n" >> imageInfo.txt
RUN printf "Source Commit: $SOURCE_COMMIT" >> imageInfo.txt

# Add entrypoint
ENTRYPOINT ["/bin/bash", "/run_read_trimmer.sh"]
