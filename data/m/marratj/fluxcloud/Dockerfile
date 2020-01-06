FROM golang:1.10.1-alpine3.7

ENV GOPATH /go

RUN mkdir -p /go/src/github.com/justinbarrick/fluxcloud

COPY . /go/src/github.com/justinbarrick/fluxcloud

WORKDIR /go/src/github.com/justinbarrick/fluxcloud

RUN apk update && apk add ca-certificates make git
RUN make test
RUN make build
RUN pwd && ls -l

FROM scratch
COPY --from=0 /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
COPY --from=0 /go/src/github.com/justinbarrick/fluxcloud/fluxcloud /fluxcloud
EXPOSE 3031
ENTRYPOINT ["/fluxcloud"]
