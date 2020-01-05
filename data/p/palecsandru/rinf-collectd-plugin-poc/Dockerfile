FROM ubuntu:16.04

# dependencies for building collectd
RUN apt-get update ; \
    apt-get install -y \
        pkg-config \
        gcc \
        make \
        python \
        python-dev \
        wget \
        libcurl4-openssl-dev

# compile collectd
RUN wget -O /tmp/collectd.tar.bz2 https://storage.googleapis.com/collectd-tarballs/collectd-5.8.0.tar.bz2
RUN mkdir /tmp/collectd
RUN tar -xjf /tmp/collectd.tar.bz2 --directory /tmp/collectd --strip 1
COPY write_http.c /tmp/collectd/src/write_http.c
RUN cd /tmp/collectd ; \
    ./configure --enable-python ; \
    make -j `cat /proc/cpuinfo | grep processor | wc -l` ; \
    make install

# other stuff
RUN mkdir -p /opt/pkb/collectd-csv
RUN mkdir -p /opt/collectd_plugins

# C plugin
COPY collectd.conf /opt
COPY start-collectd.sh /opt
RUN chmod +x /opt/start-collectd.sh

# cleanup
RUN rm -rf /tmp/collectd 
RUN rm -f /tmp/collectd.tar.bz2
RUN rm -rf /var/lib/apt/lists/*

# go to /opt when we start the container
WORKDIR /opt

### dev utils
#RUN apt-get install -y vim 