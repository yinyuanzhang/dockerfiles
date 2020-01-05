FROM golang:1.11 as builder
ENV CACHE_UPDATED=01/30/2019
RUN mkdir -p /go/src/github.com/deislabs/ && \
    git clone https://github.com/deislabs/duffle.git /go/src/github.com/deislabs/duffle
WORKDIR /go/src/github.com/deislabs/duffle
RUN make bootstrap build



FROM centos:7
RUN yum -y update && \
    yum -y install docker wget
RUN mkdir /release
COPY --from=builder /go/src/github.com/deislabs/duffle/bin/duffle /root/bin/duffle
COPY entrypoint /release/entrypoint
RUN chmod 755 /root/bin/duffle /release/entrypoint
ENV PATH=$PATH:/root/bin
WORKDIR /release
ENTRYPOINT ["/release/entrypoint"]