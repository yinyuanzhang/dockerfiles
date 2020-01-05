FROM ubuntu:14.04.4

MAINTAINER gennady.trafimenkov@gmail.com

RUN apt-get update \
 && apt-get install -y libsdl2-dev libsdl2-image-dev libpcre3-dev libfreetype6-dev libglew-dev libglm-dev libboost-filesystem-dev libpng12-dev \
 && apt-get install -y build-essential \
 && apt-get install -y wget \
 && apt-get install -y git subversion mercurial bzr \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/acaudwell/Gource/releases/download/gource-0.43/gource-0.43.tar.gz \
  && tar -xzf gource-0.43.tar.gz \
  && cd gource-0.43 \
  && ./configure \
  && make \
  && make install \
  && cd .. && rm -rf gource-0.43 gource-0.43.tar.gz

ENTRYPOINT ["/usr/local/bin/gource"]
