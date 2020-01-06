# work from latest LTS ubuntu release
FROM ubuntu:18.04

# set the environment variables
ENV mosdepth_version 0.2.5
ENV htslib_version 1.9
ENV nim_version 0.19.6

# run update
RUN apt-get update -y && apt-get install -y \
    libnss-sss \
    curl \
    less \
    vim  \
    wget \
    unzip \
    build-essential \
    libpcre3 \
    libpcre3-dev \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libnss-sss \
    libbz2-dev \
    liblzma-dev \
    bzip2 \
    libcurl4-openssl-dev \
    git \
    bwa \
    cmake


# install htslib
WORKDIR /usr/local/bin/
RUN curl -SL https://github.com/samtools/htslib/releases/download/${htslib_version}/htslib-${htslib_version}.tar.bz2 \
    > /usr/local/bin/htslib-${htslib_version}.tar.bz2
RUN tar -xjf /usr/local/bin/htslib-${htslib_version}.tar.bz2 -C /usr/local/bin/
RUN cd /usr/local/bin/htslib-${htslib_version}/ && ./configure
RUN cd /usr/local/bin/htslib-${htslib_version}/ && make
RUN cd /usr/local/bin/htslib-${htslib_version}/ && make install
ENV LD_LIBRARY_PATH /usr/local/bin/htslib-${htslib_version}/

# install nim
WORKDIR /usr/local/bin
RUN curl -SL https://nim-lang.org/download/nim-${nim_version}.tar.xz > nim-${nim_version}.tar.xz
RUN tar -xvf nim-${nim_version}.tar.xz
WORKDIR /usr/local/bin/nim-${nim_version}
RUN sh build.sh
RUN bin/nim c koch
RUN ./koch nimble
RUN ln -s /usr/local/bin/nim-${nim_version}/bin/nim /usr/local/bin/nim
RUN ln -s /usr/local/bin/nim-${nim_version}/bin/nimble /usr/local/bin/nimble

# install mosdepth
WORKDIR /usr/local/bin
RUN wget https://github.com/brentp/mosdepth/archive/v${mosdepth_version}.tar.gz
RUN tar -xzvf v${mosdepth_version}.tar.gz
WORKDIR /usr/local/bin/mosdepth-${mosdepth_version}
RUN nimble refresh
RUN nimble install -y
RUN nimble test
RUN bash functional-tests.sh
RUN nim c -d:release --cc:gcc mosdepth.nim
RUN ln -s /usr/local/bin/mosdepth-${mosdepth_version}/mosdepth /usr/local/bin/mosdepth

# set default command
WORKDIR /usr/local/bin
CMD ["mosdepth --help"]
