FROM ruby:2.2.0-wheezy

MAINTAINER Ozzy Johnson <docker@ozzy.io>

ENV DEBIAN_FRONTEND noninteractive
ENV GOLANG_VERSION 1.4.2

RUN \
    apt-get update \
        --quiet \
    && apt-get install \
        --yes \
        --no-install-recommends \
        --no-install-suggests \
    gcc \
    libc6-dev \
    make \

# Clean up packages.
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Add Go.
RUN curl -sSL https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz \
		| tar -v -C /usr/src -xz

RUN cd /usr/src/go/src && ./make.bash --no-clean 2>&1

ENV PATH /usr/src/go/bin:$PATH

RUN mkdir -p /go/src
ENV GOPATH /go
ENV PATH /go/bin:$PATH

# Get ready to build.
WORKDIR /tmp

# Build logstash-forwarder.

RUN git clone https://github.com/elasticsearch/logstash-forwarder.git

WORKDIR /tmp/logstash-forwarder

RUN gem install bundler

RUN bundle install

RUN go build

RUN make deb \
    && cp logstash-forwarder_0.4.0_amd64.deb /

VOLUME /data

CMD ["cp", "logstash-forwarder_0.4.0_amd64.deb", "/data"]
