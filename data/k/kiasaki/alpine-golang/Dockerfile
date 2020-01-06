FROM alpine:3.3
MAINTAINER Frederic Gingras <frederic@gingras.cc> (@kiasaki)

RUN apk update && apk add curl git mercurial bzr 'go=1.5.3-r0' && rm -rf /var/cache/apk/*

ENV GOROOT /usr/lib/go
ENV GOPATH /gopath
ENV GOBIN /gopath/bin
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin
