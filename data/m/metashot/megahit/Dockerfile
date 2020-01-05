FROM debian:stretch

ENV MEGAHIT_DIR /megahit
ENV MEGAHIT_TAR https://github.com/voutcn/megahit/archive/v1.1.3.tar.gz

RUN apt-get update && apt-get install -y \
    zlib1g-dev \
    python \
    g++ \
    wget \
    bc \
    make

RUN mkdir ${MEGAHIT_DIR} \
    && cd ${MEGAHIT_DIR} \
    && wget --no-check-certificate ${MEGAHIT_TAR} --output-document - |\
    tar xzf - --directory . --strip-components=1 \
    && make

ENV PATH=$PATH:${MEGAHIT_DIR}
