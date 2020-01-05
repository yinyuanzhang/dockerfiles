FROM golang:1.7
MAINTAINER e.a.agafonov@gmail.com

RUN go get github.com/tools/godep && \
    rm -Rf /go/src/github.com/tools/godep && \
    rm -Rf /go/pkg/linux_amd64/github.com/tools/godep
