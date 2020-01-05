FROM golang:1.11 AS build-env

RUN apt-get update && apt-get install -y ca-certificates

# helm
RUN wget -q -O- https://storage.googleapis.com/kubernetes-helm/helm-v2.12.1-linux-amd64.tar.gz | tar xzv -C /tmp
RUN mv /tmp/linux-amd64/helm /usr/local/bin
RUN rm -r /tmp/linux-amd64

# dep
RUN go get -u github.com/golang/dep/cmd/dep

# golint to measure code quality
RUN go get -u github.com/golang/lint/golint

# protobuf
RUN apt-get install -y libprotobuf-dev golang-goprotobuf-dev
