FROM debian:stretch

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update && apt-get install -y \
    zip \
    wget \
    libsys-hostname-long-perl \
    python \
  && rm -rf /var/lib/apt/lists/*

# Bowtie v2.3.4.3
RUN wget https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.3.4.3/bowtie2-2.3.4.3-linux-x86_64.zip \
    -q -O /tmp/bowtie2-2.3.4.3-linux-x86_64.zip
WORKDIR /tmp/
RUN unzip bowtie2-2.3.4.3-linux-x86_64.zip
RUN cp bowtie2-2.3.4.3-linux-x86_64/bowtie2* /usr/local/bin
WORKDIR /
RUN rm -rf /tmp/bowtie2-2.3.4.3-linux-x86_64.zip /tmp/bowtie2-2.3.4.3-linux-x86_64
