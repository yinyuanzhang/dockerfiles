FROM ubuntu:17.10
MAINTAINER shkawan@microsoft.com
ARG argv=00

RUN echo $argv
RUN apt update && apt install -y \
    etcd curl git
RUN curl -s -L https://redirector.gvt1.com/edgedl/go/go1.9.2.linux-amd64.tar.gz | tar xzf - -C /usr/local

RUN mkdir -p /usr/local/go/gopath
ENV GOPATH /usr/local/go/gopath
ENV PATH /usr/local/go/bin:$PATH

RUN go get github.com/skynetservices/skydns
RUN cd $GOPATH/src/github.com/skynetservices/skydns; go build -v; cp skydns /

COPY skydns.start /skydns.start
EXPOSE 53:53/udp
EXPOSE 4001:4001/tcp

CMD [ "/skydns.start" ]

