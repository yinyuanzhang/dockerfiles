FROM i386/debian:9

RUN apt-get update \
    && apt-get -y install \
      apt-utils \
      wget \
      curl \
      git \
      unzip \
      build-essential \
      libc6-dev \
      gcc-multilib \
      g++-multilib \
   && apt-get clean

WORKDIR /work
