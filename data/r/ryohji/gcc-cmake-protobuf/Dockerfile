FROM gcc:6

RUN echo "deb http://ftp.debian.org/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list \
  && apt-get update && apt-get -t jessie-backports install -y --no-install-recommends \
         cmake libarchive-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/jessie-backports.list

ADD protobuf-cpp-3.5.1.tar.gz /tmp
RUN cd /tmp/protobuf-3.5.1 && ./autogen.sh\
 && ./configure --prefix=/usr --disable-shared --with-pic\
 && make install && ldconfig\
 && rm -r /tmp/protobuf-3.5.1
