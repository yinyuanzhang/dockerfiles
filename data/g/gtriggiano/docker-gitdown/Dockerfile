FROM ubuntu:14.04

WORKDIR /gitdown

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
      build-essential \
      default-jre \
      git \
      wget \
    && rm -Rf /var/cache

RUN wget https://www.imagemagick.org/download/ImageMagick.tar.gz \
    && tar xzvf ImageMagick.tar.gz \
    && mv ImageMagick-* ImageMagick \
    && rm ImageMagick.tar.gz

RUN cd ImageMagick && ./configure && make && make install && ldconfig /usr/local/lib && cd ..

RUN git clone https://github.com/zeromq/gitdown.git repository \
    && ./repository/install-wrapper /usr/local/bin
    # && cp repository/bin/* /usr/local/bin

ADD entrypoint.sh /entrypoint
RUN chmod +x /entrypoint

WORKDIR /data

ENTRYPOINT ["/entrypoint"]
