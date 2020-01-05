FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    gcc \
    git \
    wget \
    make \
    libncurses-dev \
    flex \
    bison \
    gperf \
    python \
    python-pip \
    python-setuptools \
    python-serial \
    python-cryptography \
    python-future \
    python-pyparsing \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /esp

RUN wget -qO- https://dl.espressif.com/dl/xtensa-esp32-elf-linux64-1.22.0-80-g6c4433a-5.2.0.tar.gz | tar -xvz

ENV PATH /esp/xtensa-esp32-elf/bin:$PATH

RUN git clone --recursive https://github.com/espressif/esp-idf.git

ENV IDF_PATH /esp/esp-idf

RUN python -m pip install --user -r $IDF_PATH/requirements.txt

RUN cp -r $IDF_PATH/examples/get-started/hello_world . \
&& cd hello_world \
&& make -j8 defconfig \
&& make -j8 all \
&& cd .. \
&& rm -rf hello_world

CMD [ "/bin/bash" ]
