# Reference: https://github.com/ethereum/go-ethereum/blob/master/containers/docker/master-ubuntu/Dockerfile

FROM ubuntu:xenial

ENV PATH=/usr/lib/go-1.9/bin:$PATH

RUN \
  apt-get update && apt-get upgrade -q -y && \
  apt-get install -y --no-install-recommends golang-1.9 git make gcc libc-dev ca-certificates && \
  git clone --depth 1 --branch release/1.8 https://github.com/ethereum/go-ethereum && \
  (cd go-ethereum && make geth) && \
  cp go-ethereum/build/bin/geth /geth && \
  apt-get remove -y golang-1.9 git make gcc libc-dev && apt autoremove -y && apt-get clean && \
  rm -rf /go-ethereum

# Pull all binaries into a second stage deploy alpine container
FROM merklex/java8-jdk

COPY --from=0 /geth /usr/local/bin/

RUN apt-get update && \
    apt-get install -y curl software-properties-common git && \
    add-apt-repository -y ppa:ethereum/ethereum
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -

RUN apt-get install -y nodejs solc
RUN rm -rf /var/lib/apt/lists/*
RUN npm install ganache-cli
