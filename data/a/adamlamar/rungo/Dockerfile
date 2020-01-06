FROM buildpack-deps:stretch-scm

RUN apt-get update && apt-get install -y --no-install-recommends \
		g++ \
		gcc \
		libc6-dev \
		make \
		pkg-config \
	&& rm -rf /var/lib/apt/lists/*

ENV RUNGO_VERSION 0.0.8
ENV RUNGO_ARCH amd64

RUN curl -L -O https://github.com/adamlamar/rungo/releases/download/$RUNGO_VERSION/rungo-$RUNGO_VERSION-linux-$RUNGO_ARCH.tar.gz \
  && tar xf rungo-$RUNGO_VERSION-linux-$RUNGO_ARCH.tar.gz \
  && cp rungo /usr/local/bin \
  && ln -s /usr/local/bin/rungo /usr/local/bin/go \
  && ln -s /usr/local/bin/rungo /usr/local/bin/gofmt \
  && ln -s /usr/local/bin/rungo /usr/local/bin/godoc \
  && rm rungo-$RUNGO_VERSION-linux-$RUNGO_ARCH.tar.gz rungo

ENV GOPATH /go
ENV PATH $GOPATH/bin:$PATH

RUN mkdir -p $GOPATH/src $GOPATH/bin

# Pre-download the golang version shipped with rungo
RUN go version

WORKDIR $GOPATH
