FROM golang

ADD . /go/src/github.com/nhayes/k8s-demo

RUN go install github.com/nhayes/k8s-demo

ADD ./content /content

ENTRYPOINT /go/bin/k8s-demo
