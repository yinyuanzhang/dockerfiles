FROM centos:7 as build

RUN yum install -y \
        git \
        gcc-c++ \
        ca-certificates \
        kmod \
        wget && \
    rm -rf /var/cache/yum/*

ENV GOLANG_VERSION 1.11.5
RUN wget -nv -O - https://dl.google.com/go/go${GOLANG_VERSION}.linux-amd64.tar.gz | tar -C /usr/local -xz
ENV GOPATH /go
ENV GOBIN /go/bin
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

RUN mkdir -p /go/src/github.com/kubevirt/
WORKDIR /go/src/github.com/kubevirt/
RUN git clone https://github.com/bolkedebruin/kubernetes-device-plugins
WORKDIR /go/src/github.com/kubevirt/kubernetes-device-plugins/cmd/fuse

RUN go install fuse.go

FROM centos:7

COPY --from=build /go/bin/fuse /usr/bin/fuse

