FROM golang:1.10-alpine3.7 

ADD . /go/src/github.com/miaowukong/k8s-demo

RUN go install github.com/miaowukong/k8s-demo

ADD ./content  /content

ENTRYPOINT ["/go/bin/k8s-demo"]
