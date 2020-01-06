FROM docker:git

MAINTAINER Liu Yiding<odinushuaia@gmail.com>

# use Chinese source
RUN sed -ie 's/dl-cdn.alpinelinux.org/mirror.tuna.tsinghua.edu.cn/g' /etc/apk/repositories

# packages setup
RUN apk update
# install golang
RUN apk add go go-tools
# install make
RUN apk add make
# install bash
RUN apk add bash

# basic setup
RUN mkdir -p /opt/gocode

# environments
ENV GOROOT=/usr/lib/go
ENV GOPATH=/opt/gocode
ENV PATH=$GOROOT/bin:$GOPATH/bin:$PATH

# little trick for blocked golang.org
RUN mkdir -p $GOPATH/src/golang.org
RUN mkdir -p $GOPATH/src/github.com/golang
RUN ln -s $GOPATH/src/github.com/golang $GOPATH/src/golang.org/x

# go additional tools
RUN go get -u -v github.com/kardianos/govendor
RUN go get -u -v github.com/odinliu/got

# clean rubbish
RUN rm -rf $GOROOT/bin/darwin_* $GOROOT/bin/freebsd_* $GOROOT/bin/openbsd_* $GOROOT/bin/windows_*
