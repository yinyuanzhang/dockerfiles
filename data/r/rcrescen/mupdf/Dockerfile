FROM ubuntu:16.04

RUN apt-get update && apt-get install -y software-properties-common \
  unzip \
  build-essential python-dev python-pip wget
  
RUN wget https://mupdf.com/downloads/archive/mupdf-1.13.0-source.tar.gz -O /mupdf-source.tgz && \
    cd / && tar -zxf mupdf-source.tgz && rm mupdf-source.tgz && \
    cd /mupdf-1.13.0-source && make HAVE_X11=no HAVE_GLUT=no prefix=/usr install  && \
    rm -rf /mupdf-1.13.0-source /var/lib/apt/lists/*
