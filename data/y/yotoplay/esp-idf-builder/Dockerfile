FROM ubuntu:16.04

# Install build dependencies (and vim + picocom for editing/debugging)
RUN apt-get -qq update \
    && apt-get install -y gcc git wget make libncurses-dev flex bison gperf python python-pip zip \
                          cmake ninja-build \
                          ccache \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Get the ESP32 toolchain
ENV ESP_TCHAIN_BASEDIR /esp
ENV IDF_PATH /esp/project/esp-idf
ENV ADF_PATH /esp/project/esp-adf
RUN mkdir -p $IDF_PATH
RUN mkdir -p $ADF_PATH

RUN mkdir -p $ESP_TCHAIN_BASEDIR \
    && wget -O $ESP_TCHAIN_BASEDIR/esp32-toolchain.tar.gz \
            https://dl.espressif.com/dl/xtensa-esp32-elf-linux64-1.22.0-80-g6c4433a-5.2.0.tar.gz \
    && tar -xzf $ESP_TCHAIN_BASEDIR/esp32-toolchain.tar.gz \
           -C $ESP_TCHAIN_BASEDIR/ \
    && rm $ESP_TCHAIN_BASEDIR/esp32-toolchain.tar.gz \
    && git clone -b v3.2.2 --recursive https://github.com/espressif/esp-idf.git $IDF_PATH \
    && git clone --recursive https://bitbucket.org/yotoplay/esp-adf.git $ADF_PATH \
    && rm -rf $ADF_PATH/esp-idf \
    # ADD the esp-adf commit sha to text file
    && echo `cd $ADF_PATH; git rev-parse HEAD` > /esp/project/ADF_SHA \ 
    # ADD the esp-idf commit sha to text file
    && echo `cd $IDF_PATH; git rev-parse HEAD` > /esp/project/IDF_SHA

RUN pip install --user -r $IDF_PATH/requirements.txt

# Add the toolchain binaries to PATH
ENV PATH $ESP_TCHAIN_BASEDIR/xtensa-esp32-elf/bin:$IDF_PATH/tools:$PATH
# This is the directory where our project will show up
WORKDIR /esp/project
ENTRYPOINT ["idf.py"]