FROM golang:1.12

WORKDIR $GOPATH/src/github.com/k8s

ADD . $GOPATH/src/github.com/k8s

ENV GO111MODULE on

ENV GOPROXY https://athens.azurefd.net

RUN go build .

ENTRYPOINT  ["./k8s"]