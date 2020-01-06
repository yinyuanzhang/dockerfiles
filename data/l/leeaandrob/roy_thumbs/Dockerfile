FROM centos:latest as builder

RUN yum update -y && yum upgrade -y
RUN yum install -y wget git
RUN  yum group install -y "Development Tools"
RUN wget https://dl.google.com/go/go1.11.2.linux-amd64.tar.gz && sha256sum go1.11.2.linux-amd64.tar.gz && tar -C /usr/local -xzf go1.11.2.linux-amd64.tar.gz

RUN echo "export GO111MODULE=on" >> /root/.bash_profile && echo "export PATH=$PATH:/usr/local/go/bin" >> /root/.bash_profile
RUN source /root/.bash_profile

WORKDIR /repo
COPY . /repo/
RUN /usr/local/go/bin/go build /repo/./
