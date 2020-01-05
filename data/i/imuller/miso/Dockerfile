FROM ubuntu:18.04
MAINTAINER Ittai Muller i.muller@vumc.nl adapted from Nuno Agostinho <nunodanielagostinho@gmail.com>

ENV TZ=Europe/Amsterdam
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update

# samtools
# Usage: samtools [OPTIONS]
RUN apt-get install -y gcc
RUN apt-get install -y libncurses5-dev
RUN apt-get install -y libbz2-dev
RUN apt-get install -y liblzma-dev
RUN apt-get install -y libcurl4-openssl-dev
RUN apt-get install -y libssl-dev
RUN apt-get install -y zlib1g-dev
RUN apt-get install -y make

ENV SW=/root/software
WORKDIR ${SW}

ENV samtools=samtools-1.9
ADD ${samtools}.tar.bz2 .
ADD miso_settings.txt .
WORKDIR ${samtools}

RUN ./configure
RUN make
RUN make install
WORKDIR ${SW}

# MISO
# Usage: miso [OPTIONS]
# For instance, miso --run

RUN apt update
RUN apt install -y python-pip
RUN pip install --upgrade pip
RUN apt install -y python3-numpy
RUN apt install -y python3-scipy
RUN apt install -y python3-matplotlib
RUN apt-get install -y python-dev
RUN apt-get install -y build-essential
RUN apt-get install -y bedtools

RUN pip install misopy
ADD miso_settings.txt .
