FROM debian:buster-slim

RUN apt-get update -qq
RUN apt-get install -y \
  wget \
  gcc \
  zlib1g-dev \
  make

RUN wget -nv \
  https://sourceforge.net/projects/subread/files/subread-1.6.3/subread-1.6.3-source.tar.gz/download \
  -O subread.tar.gz

RUN tar xzf subread.tar.gz \
  && cd subread-1.6.3-source/src \
  && make -f Makefile.Linux \
  && mv ../bin/featureCounts /usr/local/bin
