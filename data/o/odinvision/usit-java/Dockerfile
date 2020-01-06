FROM ubuntu:18.04

RUN apt-get update && apt-get install -y software-properties-common build-essential wget unzip cmake python-numpy python-dev

RUN mkdir /opt/install
WORKDIR /opt/install

# install opencv
RUN wget https://github.com/opencv/opencv/archive/2.4.13.6.zip \
    && unzip 2.4.13.6.zip \ 
    && mkdir opencv-2.4.13.6/build \
    && cd opencv-2.4.13.6/build \
    && cmake ../ && make -j $(nproc) install

# install boost 
RUN wget https://sourceforge.net/projects/boost/files/boost/1.59.0/boost_1_59_0.zip \
    && unzip boost_1_59_0.zip \
    && cd boost_1_59_0 \
    && ./bootstrap.sh --prefix=/usr/local \
    && ./b2 -j $(nproc) --with-filesystem --with-system --with-regex install

# install usit
RUN mkdir /opt/usit && mkdir usit-src
COPY . usit-src
RUN mkdir usit-build \
    && cd usit-build \
    && cmake ../usit-src \ 
    && make && make test \
    && make install \
    && cp hd lg wahet /opt/usit

FROM ubuntu:18.04

LABEL maintainer="slava.goronostal@gmail.com"

COPY --from=0 /usr/local/lib /usr/local/lib
COPY --from=0 /opt/usit /opt/usit

RUN apt-get update \
    && apt-get install -y openjdk-11-jre \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean -y
