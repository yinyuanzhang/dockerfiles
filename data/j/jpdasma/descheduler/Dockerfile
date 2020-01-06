FROM golang:1.11.2-alpine3.8

ARG VERSION=0.8.0

RUN mkdir -p /go/src/github.com/kubernetes-incubator/

ADD https://github.com/kubernetes-incubator/descheduler/archive/v${VERSION}.tar.gz /go/src/github.com/kubernetes-incubator/

WORKDIR /go/src/github.com/kubernetes-incubator/

RUN tar -xf v${VERSION}.tar.gz && \
    mv descheduler-${VERSION} descheduler 

WORKDIR descheduler

RUN go build cmd/descheduler/descheduler.go

FROM alpine:3.8

COPY --from=0 /go/src/github.com/kubernetes-incubator/descheduler/descheduler /bin/descheduler

CMD ["/bin/descheduler", "--help"]
