FROM golang:1.11.1-alpine3.7
ENV GOPATH "/go:/go/src/github.com/arilot/k8s-statefulset-pv-precreator"

RUN apk --update add git openssh gcc make g++ pkgconfig zlib-dev bash

RUN go get -u k8s.io/client-go/...
RUN go get -u github.com/aws/aws-sdk-go/...

ADD src /go/src/github.com/arilot/k8s-statefulset-pv-precreator/src
WORKDIR /go/src/github.com/arilot/k8s-statefulset-pv-precreator/src

RUN go build -o /usr/sbin/init-container /go/src/github.com/arilot/k8s-statefulset-pv-precreator/src/cmd/init-container.go

RUN rm -rf /go/src