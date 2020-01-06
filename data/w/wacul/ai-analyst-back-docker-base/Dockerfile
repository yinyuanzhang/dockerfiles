FROM python:3.7-slim

# required packages
RUN apt-get update && apt-get install -y --force-yes --no-install-recommends \
    curl \
    git \
    openssh-client \
    g++ \
    gcc \
    libc6-dev \
    make \
    pkg-config \
    libsasl2-dev \
    musl-dev \
    jq \
    libperl-dev \
    gfortran \
    liblapack-dev \
    apt-transport-https \
    ca-certificates \
    gnupg2 \
    software-properties-common \
    upx \
  && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | apt-key add - \
  && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") $(lsb_release -cs) stable" \
  && apt-get update && apt-get install -y docker-ce

ENV GOLANG_VERSION 1.12.5
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-amd64.tar.gz
ENV GOLANG_DOWNLOAD_SHA256 aea86e3c73495f205929cfebba0d63f1382c8ac59be081b6351681415f4063cf

RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \
  && echo "$GOLANG_DOWNLOAD_SHA256  golang.tar.gz" | sha256sum -c - \
  && tar -C /usr/local -xzf golang.tar.gz \
  && rm golang.tar.gz

ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

COPY requirements.txt /

RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" \
    && chmod -R 777 "$GOPATH" \
    && pip install --no-cache-dir -r /requirements.txt && rm /requirements.txt \
    && pip install --no-binary :all: pymongo==3.4.0 \
    # set timezone to Asia/Tokyo
    && ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
    && dpkg-reconfigure --frontend noninteractive tzdata

RUN    go get -v golang.org/x/lint/golint \
    && go get -v golang.org/x/tools/cmd/goimports \
    && go get -v github.com/tsenart/deadcode \
    && go get -v github.com/kisielk/errcheck \
    && go get -v honnef.co/go/tools/cmd/staticcheck \
    && go get -v github.com/gordonklaus/ineffassign \
    && go get -v github.com/kyoh86/scopelint \
    && go get -v github.com/opennota/check/cmd/aligncheck \
    && go get -v github.com/opennota/check/cmd/structcheck \
    && go get -v github.com/opennota/check/cmd/varcheck \
    && go get -v github.com/mdempsky/unconvert \
    && go get -v honnef.co/go/tools/cmd/gosimple \
    && go get -v github.com/jgautheron/goconst/cmd/goconst

WORKDIR $GOPATH
