FROM golang:1.11

RUN apt-get -y -qq update && apt-get -y -qq install build-essential \
  make pkgconf wget ca-certificates  \
  openssl git libssh2-1-dev
RUN GLIDE_VERSION=v0.12.3 ARCH=linux-amd64 && \
    mkdir -p /tmp/glide && \
    cd /tmp/glide && \
    curl -SsL https://github.com/Masterminds/glide/releases/download/${GLIDE_VERSION}/glide-${GLIDE_VERSION}-${ARCH}.tar.gz | \
    tar -xvz && \
    install -d $GOPATH/bin; \
    install -m 755 ./${ARCH}/glide $GOPATH/bin && \
    rm -rf /tmp/glide
RUN mkdir -p /go/tmp && \
  pkg-config --cflags freexl || cd /go/tmp  && \
    wget -c "http://www.gaia-gis.it/gaia-sins/freexl-sources/freexl-1.0.2.tar.gz" && \
    tar -xvzf freexl-*.tar.gz && \
    cd freexl-*/ && \
    ./configure --prefix=/usr && \
    make && \
    make install && \
    make clean && \
    cd /go ; \
  rm -rf /go/tmp /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN mkdir -p /go/tmp && pkg-config --cflags libcurl || \
    cd /go/tmp && \
    wget -c https://curl.haxx.se/download/curl-7.49.1.tar.gz && \
    tar -xvzf curl-*.tar.gz && \
    cd curl-*/ && \
    ./configure --prefix=/usr --with-libssh2 --with-ssl && \
    make && \
    make install && \
    make clean && \
    cd /go ; \
  rm -rf /go/tmp /var/lib/apt/lists/* /tmp/* /var/tmp/*