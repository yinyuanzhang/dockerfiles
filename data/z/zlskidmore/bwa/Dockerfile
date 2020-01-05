# work from latest LTS ubuntu release
FROM ubuntu:18.04

# set the environment variables
ENV bwa_version 0.7.17

# run update and install necessary tools ubuntu tools
RUN apt-get update -y && apt-get install -y \
    build-essential \
    libz-dev \
    unzip \
    curl \
    libnss-sss \
    vim \
    less

# download bwa
WORKDIR /usr/local/bin/

RUN mkdir -p /usr/local/bin/ \
  && curl -SL https://github.com/lh3/bwa/archive/v${bwa_version}.zip \
  >  v${bwa_version}.zip
RUN unzip v${bwa_version}.zip && rm -f v${bwa_version}.zip
RUN cd /usr/local/bin/bwa-${bwa_version} && make
RUN ln -s /usr/local/bin/bwa-${bwa_version}/bwa /usr/local/bin
