FROM centos:7

RUN yum -y update && yum clean all

RUN yum -y install epel-release

RUN mkdir -p /go && chmod -R 777 /go && \
    yum -y install git golang && yum clean all


ENV GOPATH /go

WORKDIR /go

ENV PATH="/go/bin:${PATH}"
RUN mkdir -p /go/bin
RUN curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh
