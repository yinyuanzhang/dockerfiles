FROM ubuntu:18.04

# Based on https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/get-started/linux-setup.html

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
    python-serial \
    python-pip \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /esp

RUN wget -qO- https://dl.espressif.com/dl/xtensa-lx106-elf-linux64-1.22.0-92-g8facf4c-5.2.0.tar.gz | tar -xvz

ENV PATH /esp/xtensa-lx106-elf/bin:$PATH

RUN git clone --recursive https://github.com/espressif/ESP8266_RTOS_SDK.git

ENV IDF_PATH /esp/ESP8266_RTOS_SDK

RUN python -m pip install --user -r $IDF_PATH/requirements.txt

RUN cp -r $IDF_PATH/examples/get-started/project_template . \
&& cd project_template \
&& make -j8 defconfig \
&& make -j8 all \
&& cd .. \
&& rm -rf project_template

CMD [ "/bin/bash" ]
